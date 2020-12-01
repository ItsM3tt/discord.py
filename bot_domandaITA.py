import discord
import random
from discord.ext import commands #command extension

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():            #when the bot is ready
    print('Bot is ready.')

@client.command()
async def ping(ctx):             #ctx = context
    await ctx.send(f'Pong! Ci ho messo {round(client.latency * 1000)}ms per rispondere, un pò troppo dio merda.')

@client.command()
async def domandina(ctx, *, domanda):
    risposte = ['Certo.',
                 'È certamente così.',
                 'Senza dubbio.',
                 'Ovvio',
                 'Si.',
                 'La mia bolla di vetro dice di si.',
                 'Mh sembra di si.',
                 'Sembra di si.',
                 'iS.',
                 '!= no.',
                 'Riprova zzi.',
                 'Richiedimelo dopo.',
                 'Meglio se non te lo dica.',
                 'Non posso predictare una cazzata del genere.',
                 'Richiedimelo dopo.',
                 'No.',
                 'Nope.',
                 'Direi di no.']

    await ctx.send(f'Domanda: {domanda}\nRisposta: {random.choice(risposte)}')

client.run('NzczNjQzODcwOTM2MjM2MDU0.X6MOAA.6c8_JY6GCDkRvxHoSxjEWKxvzwA') #running the bot with it's token
