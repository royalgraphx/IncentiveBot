# IncentiveBot
I wondered if it was possible to fully create a Discord bot with only using Chat-GPT3. The goal being, I've wanted to make "Mmm" a more common term among my friends, so to incentivize it, it rewards people with XP. It can of course be used for other things like grammar and so on.

This currently runs off of my RPI4 Pi-Hole/Pi-VPN/PXE Boot/NAS at home. Simply install Python and use pip3 to get discord.py

Then run start.py


Features:

- Positive Words List - Any word in this text document gets a '✅' reaction.
- Negative Words List - Any word in this text document gets a '❌' reaction.
- Leaderboard - use the !leaderboard command to print out a Top 10 of the most XP!
