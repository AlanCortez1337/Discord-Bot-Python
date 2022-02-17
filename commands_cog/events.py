import discord
import re
import random
import os
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

class TEXTEVENTS(commands.Cog):

    def __init__(self, bot):
        self.client = bot
    # just a booting message claiming that this cog is properly working
    @commands.Cog.listener()
    async def on_ready(self):
        print("text events: Active")
    # Beginning of listener event commands
    # ANNOYING "YOUR" EVENT
    @commands.Cog.listener("on_message")
    async def yourWrong(self, message):
        chanceOfCorrection = random.randint(1,20)
        input = message.content
        if message.author.bot:
            return
        # CHECKS IF SOMEONE'S MESSAGE INCLUDES A FORM OF YOUR
        # CHECKS VIA REGEX PATTERN AND IF IT PASSES THEN SENDS THE GIF
        # should cover "your, you're, ur, u r" and an arrangment of those forms
        if (re.search(r'(you|^u| u)+(\s(ar|r)|\'|r[e.?! ]|r$)', input, re.I)):
            # Before sending the annoying gif I made it specifically always send
            # whenever the 'TARGET-PERSON' sent a message containing the word
            # "your" but a 1/20 chance for everyone else
            if message.author.id == int(os.getenv('TARGET-PERSON')):
                await message.channel.send('https://tenor.com/view/youre-spelling-mistake-metal-gear-rising-itsyoure-gif-23889242')
            elif chanceOfCorrection == 20:
                await message.channel.send('https://tenor.com/view/youre-spelling-mistake-metal-gear-rising-itsyoure-gif-23889242')
    # RANDOM EMOJI REACTION EVENT
    @commands.Cog.listener("on_message")
    async def emojiReaction(self, message):
        luckyNum = random.randint(1, 20)
        if luckyNum == 20:
            await message.add_reaction('😳')
        elif luckyNum == 1:
            await message.add_reaction('😨')
    # LOAD SUCCESSFUL
    @commands.Cog.listener("on_message")
    #TODO:
    #fix permissions
    #add comments about the loadWords for loop thing
    @commands.has_role("Big Cheeses")
    async def successfulExecution(ctx, message):
        input = message.content

        loadWords = ['reload', 'load', 'unload']
        for words in loadWords:
            if not (message.author.guild_permissions.administrator):
                await message.add_reaction('👎')
            elif ("mister please %s" %(words)) in input:
                await message.add_reaction('👍')

def setup(bot):
    bot.add_cog(TEXTEVENTS(bot))
