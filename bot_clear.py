import discord
from discord.ext import commands #command extension

client = commands.Bot(command_prefix = '/')

'''
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
n_end = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
'''

@client.event
async def on_ready():       #when the bot is ready
    print('Bot is ready.')
    

@client.command()
async def clear(ctx, amount = 20):         #clear = command / [ctx = context of the command / amount = amount of messages we want to delete] these are parameters
    await ctx.message.delete()
    await ctx.channel.purge(limit = amount)

'''
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('/clear') and message.content.endswith(tuple(n_end)):
        await client.delete_messages(messages)
'''

client.run('NzczNjQzODcwOTM2MjM2MDU0.X6MOAA.6c8_JY6GCDkRvxHoSxjEWKxvzwA') #running the bot with it's token
    
 
