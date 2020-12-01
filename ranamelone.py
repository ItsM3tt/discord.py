import discord
import random
import os
from discord.ext import commands #C  ommand extension


client = commands.Bot(command_prefix = '/')
parole_rana = ['frog', 'rana', 'ronny', 'ronni', 'rana melone', 'ranamelone', 'ranaldo', '@Rana Melone', '@RanaMelone#6030']
parole_lollo = ['lollo', 'Loco', 'Lo Curto', 'locurto', 'lorenzo', '@lory_268']
parole_materialmente = ['materialmente', 'bonadonna', 'riky', 'meccanica']


@client.event
async def on_ready():            #When the bot is ready
    print('Bot is online.')


@client.command()
async def rana(ctx):
    await ctx.send(file=discord.File('ranamelone1.png'))


@client.event
async def on_message(message):
    
    message.content = message.content.lower().replace(' ', '')
    
    for i in range(len(parole_rana)):
        if parole_rana[i] in message.content:
            await message.channel.send(file = discord.File('ranamelone1.png'))

    for i in range(len(parole_lollo)):
        if parole_lollo[i] in message.content:
            await message.channel.send(file = discord.File('lollo.png'))

    for i in range(len(parole_materialmente)):
        if parole_materialmente[i] in message.content:
            await message.channel.send(file = discord.File(random.choice(("bonadonna1.png", "bonadonna2.png"))))


client.run('NzczNjQzODcwOTM2MjM2MDU0.X6MOAA.6c8_JY6GCDkRvxHoSxjEWKxvzwA') #Running the bot with it's token
