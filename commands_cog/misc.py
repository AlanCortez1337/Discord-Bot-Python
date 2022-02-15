import discord
import re
from discord.ext import commands

class MISC(commands.Cog):

    def __init__(self, bot):
        self.client = bot
    # Beginning of misc commands I made for this bot.
    # CURRENTLY NO COMMANDS FOR THIS FOLDER, SOON THOUGH
    @commands.Cog.listener()
    async def on_ready(self):
        print("misc commands: Active")

    # Need to find a way where only a person with permision can execute this
    # @commands.command()
    # async def wipe(self, ctx, amount=5):
    #     print(ctx,amount)
    #     #await ctx.channel.purge(limit = amount)

def setup(bot):
    bot.add_cog(MISC(bot))
