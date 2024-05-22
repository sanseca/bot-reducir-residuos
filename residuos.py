import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'has iniciado sesion {bot.user}')

@bot.command()
async def manualidades(ctx):
    ej = ["ladrillos ecologicos", "lapicero", "silla recicladora"]
    await ctx.send(random.choice(ej))

@bot.command()
async def ideas(ctx):
    id = ["usar botellas reciclables", "usar bolsas reutilizables", "dona lo que ya no usas."]
    await ctx.send(random.choice(id))


bot.run("token")
