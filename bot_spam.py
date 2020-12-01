import discord
import random
import asyncio 
from discord.ext import commands #command extension
from discord.ext.commands import CommandNotFound

client = commands.Bot(command_prefix = '/')


@client.event
async def on_ready():            #when the bot is ready
    print('Bot is ready.')

@client.command()
async def ping(ctx):             #ctx = context
    await ctx.send(f'Pingo {round(client.latency * 1000)}')

    
@client.command()
async def spam(ctx):
    await ctx.send('Scrivi un numero alla fine del comando `/spam` (es. /spam3) per spammare un determinato numero di volte.')
@client.command()
async def spam1(ctx):
    for i in range(1):
        await ctx.send('Cazzo ti serve spammare una volta? Oh, non ti avevo riconosciuto, riprenditi questi...')
        await asyncio.sleep(3)
        await ctx.send(file = discord.File('clown_wig.png'))
        await ctx.send(file = discord.File('clown_nose.png'))
@client.command()
async def spam2(ctx, *, spammettino):
    for i in range(2):
        await ctx.send(f'{spammettino}')
@client.command()
async def spam3(ctx, *, spammettino):
    for i in range(3):
        await ctx.send(f'{spammettino}')
@client.command()
async def spam4(ctx, *, spammettino):
    for i in range(4):
        await ctx.send(f'{spammettino}')
@client.command()
async def spam5(ctx, *, spammettino):
    for i in range(5):
        await ctx.send(f'{spammettino}')
@client.command()
async def spam6(ctx, *, spammettino):
    for i in range(6):
        await ctx.send(f'{spammettino}')
@client.command()
async def spam7(ctx, *, spammettino):
    for i in range(7):
        await ctx.send(f'{spammettino}')
@client.command()
async def spam8(ctx, *, spammettino):
    for i in range(8):
        await ctx.send(f'{spammettino}')
@client.command()
async def spam9(ctx, *, spammettino):
    for i in range(9):
        await ctx.send(f'{spammettino}')
@client.command()
async def spam10(ctx, *, spammettino):
    for i in range(10):
        await ctx.send(f'{spammettino}')
@client.command()
async def spam11(ctx, *, spammettino):
    for i in range(1):
        await ctx.send('Non mi intasare il server')
@client.command()
async def spam12(ctx, *, spammettino):
    for i in range(1):
        await ctx.send('Non mi intasare il server')
@client.command()
async def spam13(ctx, *, spammettino):
    for i in range(1):
        await ctx.send('Non mi intasare il server')
@client.command()
async def spam14(ctx, *, spammettino):
    for i in range(1):
        await ctx.send('Non mi intasare il server')
@client.command()
async def spam15(ctx, *, spammettino):
    for i in range(1):
        await ctx.send('Non mi intasare il server')
@client.command()
async def spam16(ctx, *, spammettino):
    for i in range(1):
        await ctx.send('Non mi intasare il server')
@client.command()
async def spam17(ctx, *, spammettino):
    for i in range(1):
        await ctx.send('Non mi intasare il server')
@client.command()
async def spam18(ctx, *, spammettino):
    for i in range(1):
        await ctx.send('Non mi intasare il server')
@client.command()
async def spam19(ctx, *, spammettino):
    for i in range(1):
        await ctx.send('Non mi intasare il server')
@client.command()
async def spam20(ctx, *, spammettino):
    for i in range(1):
        await ctx.send('Non mi intasare il server')
@client.command()
async def spam21(ctx, *, spammettino):
    for i in range(1):
        await ctx.send('Non mi intasare il server')
@client.command()
async def spam22(ctx, *, spammettino):
    for i in range(1):
        await ctx.send('Non mi intasare il server')
@client.command()
async def spam23(ctx, *, spammettino):
    for i in range(1):
        await ctx.send('Non mi intasare il server')
@client.command()
async def spam24(ctx, *, spammettino):
    for i in range(1):
        await ctx.send('Non mi intasare il server')
@client.command()
async def spam25(ctx, *, spammettino):
    for i in range(1):
        await ctx.send('Non mi intasare il server')
@client.command()
async def spam26(ctx, *, spammettino):
    for i in range(1):
        await ctx.send('Non mi intasare il server')
@client.command()
async def spam27(ctx, *, spammettino):
    for i in range(1):
        await ctx.send('Non mi intasare il server')
@client.command()
async def spam28(ctx, *, spammettino):
    for i in range(1):
        await ctx.send('Non mi intasare il server')
@client.command()
async def spam29(ctx, *, spammettino):
    for i in range(1):
        await ctx.send('Non mi intasare il server')
@client.command()
async def spam30(ctx, *, spammettino):
    for i in range(1):
        await ctx.send('Non mi intasare il server')

'''
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send('Non mi intasare il server')
'''
        
client.run('NzczNjQzODcwOTM2MjM2MDU0.X6MOAA.6c8_JY6GCDkRvxHoSxjEWKxvzwA') #running the bot with it's token
