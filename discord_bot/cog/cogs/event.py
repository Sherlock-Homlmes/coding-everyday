import discord
from discord.ext import commands

import json

prefix = ["test,","Test,"]

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is ready.")
        await self.bot.change_presence(activity=discord.Game(name=f"{prefix} - prefix"))


def setup(bot):
    bot.add_cog(Events(bot))