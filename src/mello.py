import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# guardando permissões de intents
intents = discord.Intents.all()
bot = commands.Bot("!", intents=intents)

@bot.event
async def on_ready():
    print("O bot está pronto!")

@bot.command()
# ctx guarda o contexto da mensagem, processando o comando | tipamos o comando mello com o tipo commands.Context que é o tipo de dado que o discord.py espera
# o decorator @bot.command() transforma a função mello em um comando do bot
async def mello(ctx:commands.Context):
    nome = ctx.author.display_name
    await ctx.reply(f"Olá {nome} Como posso ajudar você?")
    
@bot.command()    
async def say(ctx:commands.Context, *text):
    await ctx.send(text)
    
@bot.command()
async def some(ctx:commands.Context, num1:int, num2:int):
    resultado = num1 + num2
    await ctx.send(f"O resultado da soma é: {resultado}")
    
    alteração qualquer


load_dotenv()
bot.run(os.getenv("TOKEN"))
