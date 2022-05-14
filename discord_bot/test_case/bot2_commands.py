import discord
import asyncio
from discord.ext import commands

from dotenv import load_dotenv

from multi_bots import bot2

@bot2.event
async def on_ready():
    print('Logged in as')
    print(bot2.user.name)
    print(bot2.user.id)
    print(' ')
