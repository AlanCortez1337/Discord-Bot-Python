import discord
import random
from discord.ext import commands

class Random(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("random commands: Active")

    # INDECISIVE CHOICE COMMAND
    @commands.command() # helps you pick through your choices
    async def choose(self, ctx, *, input):
        # Takes in the message the user sent after calling this command and
        # storing the result in a list in order to randomly select from the options
        choices = input.split(" ")
        if len(choices) == 1:
            await ctx.send(f'Really? it seems like you can only do: {input}')
        else:
            # Since a list is anywhere from 0 to 1 we need to consider this
            # which is why we have len(choices) - 1
            randChoice = random.randint(0, len(choices)-1)
            await ctx.send(f'I choose that you do: {choices[randChoice]}')


    # ROLL FOR ME
    @commands.command()
    # input is !roll d#
    async def roll(self, ctx, *, input):
        #add a feature to celebrate if it is the max or min number
        inputSize = len(input)

        if input[0] == "d":
            die = input[1:inputSize]
            if (int(die) == 4) or (int(die) == 6) or (int(die) == 8) or (int(die) == 10) or (int(die) == 12) or (int(die) == 20) or (int(die) == 100):
                randDie = random.randint(1, int(die))
                await ctx.send(f'You rolled a: {randDie}')
            else:
                await ctx.send('Invalid number, try again')
        else:
            randNum = random.randint(1, int(input))
            await ctx.send(f'You rolled a: {randNum}')

def setup(bot):
    bot.add_cog(Random(bot))
