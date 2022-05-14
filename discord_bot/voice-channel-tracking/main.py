from dotenv import load_dotenv
from discord_bot import bot
import os

from threading import Thread
import time



load_dotenv()
my_secret = os.environ['BOT_TOKEN']
bot.run(my_secret)