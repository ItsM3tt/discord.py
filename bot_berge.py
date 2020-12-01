import discord
import random
import os
from discord.ext import commands #C  ommand extension


client = commands.Bot(command_prefix = '/')
parole_m3tt = ['berge']


@client.event
async def on_ready():            #When the bot is ready
    print('Bot is online.')


@client.event
async def on_message(message):

    message.content = message.content.lower().replace(' ', '')

    for i in range(len(parole_m3tt)):
        if message.author == client.user:
            return
        if parole_m3tt[i] in message.content:
            await message.delete()
            await message.channel.send('{}, chiamami un\'altra volta così e vedi'.format(message.author.mention))


client.run('NzczNjQzODcwOTM2MjM2MDU0.X6MOAA.6c8_JY6GCDkRvxHoSxjEWKxvzwA') #Running the bot with it's token
