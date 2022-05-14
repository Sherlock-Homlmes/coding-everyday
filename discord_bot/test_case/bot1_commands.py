import discord
import asyncio
from discord.ext import commands

from dotenv import load_dotenv

from multi_bots import bot1

@bot1.event
async def on_ready():
    print('Logged in as')
    print(bot1.user.name)
    print(bot1.user.id)
    print(' ')