#!/usr/bin/python

#
# IncentiveBot, compiled by RoyalGraphX with assistance from Chat-GPT 3
#

import os
import discord
import json
from discord.ext import commands

xp_data = {}

# API Key
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Load words that should receive a "✅" reaction
positive_words = []
if os.path.exists('positive_words.txt'):
    with open('positive_words.txt', 'r') as f:
        for line in f:
            positive_words.append(line.strip())

# Load words that should receive a "❌" reaction
negative_words = []
if os.path.exists('negative_words.txt'):
    with open('negative_words.txt', 'r') as f:
        for line in f:
            negative_words.append(line.strip())

# Load XP data from file
user_xp = {}
if os.path.exists('user_xp.json'):
    with open('user_xp.json', 'r') as f:
        user_xp = json.load(f)

# Save XP data to file
def save_user_xp():
    with open('user_xp.json', 'w') as f:
        json.dump(user_xp, f)

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    global user_xp

    print(f'Message received from {message.author.name}: {message.content}')
    
    # Check if message contains a positive word
    if any(word in message.content.split() and word in positive_words for word in message.content.split()):
        await message.add_reaction('✅')
        print(f'Added reaction to message from {message.author.name}: {message.content}')
        
        # Add XP to user
        user_id = str(message.author.id)
        if user_id not in user_xp:
            user_xp[user_id] = 0
        user_xp[user_id] += 1
        save_user_xp()
        print(f'{message.author.name} gained 1 XP! Total XP: {user_xp[user_id]}')

    # Check if message contains a negative word
    if any(word in message.content.split() and word in negative_words for word in message.content.split()):
        await message.add_reaction('❌')
        print(f'Added reaction to message from {message.author.name}: {message.content}')

@bot.command(name='leaderboard')
async def leaderboard(ctx):
    global user_xp

    sorted_users = sorted(user_xp.items(), key=lambda x: x[1], reverse=True)

    leaderboard = []
    for i, (user_id, xp) in enumerate(sorted_users):
        user = await bot.fetch_user(int(user_id))
        leaderboard.append(f'{i+1}. {user.name}: {xp} XP')

    await ctx.send('**Leaderboard**\n' + '\n'.join(leaderboard[:10]))

bot.run('YOUR_BOT_API_KEY_HERE')
