import discord
from discord.ext import commands

class Music(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("music commands: Active")

def setup(bot):
    bot.add_cog(Music(bot))
