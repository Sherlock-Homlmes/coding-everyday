import discord
import asyncio
from discord.ext import commands

from dotenv import load_dotenv

bot = [0,1]
bot_token = [
#book
'OTY4NDQyMzQ1MDk3OTUzMzAw.Yme6Nw.BBqqV2Xpujb1cA_Ur9jJiJvN770',
#scary
'OTY4NDQyMTI5MTkxOTUyMzk0.Yme6BA.oeHhJwMpJIM2EaqIR_2U7N-f1YU',
#funny
'OTY4NDQyMjI1NTY4Njc3OTI4.Yme6Gw.wIRSPFoduFQbYwxcwiHP3RT9ZU4',
]

#book bot
bot0 = commands.Bot(command_prefix = 'bot0,')

#scary bot
bot1 = commands.Bot(command_prefix = 'bot1,')

#funny bot
bot2 = commands.Bot(command_prefix = 'bot2,')

#import bot commands
from bot0_commands import *
from bot1_commands import *
from bot2_commands import *
