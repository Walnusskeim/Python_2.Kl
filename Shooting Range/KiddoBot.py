'''
a not very friendly Discord bot
Maximilian
03.01.2023
'''

#bot.py
import os

import discord

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord baby!')

client.run(TOKEN)

