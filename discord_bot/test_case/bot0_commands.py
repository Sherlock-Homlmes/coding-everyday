
import discord
import asyncio
from discord.ext import commands

from dotenv import load_dotenv

from multi_bots import bot0

@bot0.event
async def on_ready():
    print('Logged in as')
    print(bot0.user.name)
    print(bot0.user.id)
    print(' ')

