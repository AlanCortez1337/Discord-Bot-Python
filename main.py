import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix = 'mister please ')
# @commands.command()
# async def ping(self, ctx):
#     await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('Buy more Bitcoin!'))
    print('bot: Active')

# Error checks if user incorrectly uses a command
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please include additional information for the command')

@bot.command()
async def load(ctx, extension):
    print('loaded: ',extension)
    bot.load_extension(f'commands_cog.{extension}')

@bot.command()
async def unload(ctx, extension):
    print('unloaded: ',extension)
    bot.unload_extension(f'commands_cog.{extension}')

@bot.command()
async def reload(ctx, extension):
    print('reloaded: ',extension)
    bot.unload_extension(f'commands_cog.{extension}')
    bot.load_extension(f'commands_cog.{extension}')

for filename in os.listdir('./commands_cog'):
    if filename.endswith('.py'):
        bot.load_extension(f'commands_cog.{filename[:-3]}')

bot.run('ODUxNTQ1MDMwMjM4MDExNDEy.YL51HA.hmidiV1LNmmEBe8Ntb4Zksy594E')
