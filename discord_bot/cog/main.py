import discord
from discord.ext import commands, tasks
from discord_slash import SlashCommand,SlashContext
from discord_slash.utils.manage_commands import create_option
import os
from dotenv import load_dotenv
import json
load_dotenv()

bot = commands.Bot(command_prefix=["test,","Test,"])

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")



my_secret = os.environ['BOT_TOKEN']
bot.run(my_secret) 
