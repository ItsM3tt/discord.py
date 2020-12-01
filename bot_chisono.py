import discord
import random
import os
from discord.ext import commands #C  ommand extension


client = commands.Bot(command_prefix = '/')


@client.event
async def on_ready():            #When the bot is ready
    print('Bot is online.')


@client.command()
async def chisono(ctx):
    await ctx.send('Tu sei {}'.format(ctx.author.name))


client.run('NzczNjQzODcwOTM2MjM2MDU0.X6MOAA.6c8_JY6GCDkRvxHoSxjEWKxvzwA') #Running the bot with it's token
