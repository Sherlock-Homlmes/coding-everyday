import discord
import asyncio
from discord.ext import commands

from dotenv import load_dotenv

from multi_bots import *

loop = asyncio.get_event_loop()
loop.create_task(bot0.start(bot_token[0]))
loop.create_task(bot1.start(bot_token[1]))
loop.create_task(bot2.start(bot_token[2]))
loop.run_forever()
