import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio
from aioconsole import ainput


# guardando permissões de intents
intents = discord.Intents.all()
bot = commands.Bot("!", intents=intents)


@bot.event
async def on_ready():
    print("O bot está pronto!")
    asyncio.create_task(reiniciarBot())

async def reiniciarBot():
    while True:
        res = await ainput("Digite 's' para reiniciar o bot ou 'e' para sair: ")
        try: 
            if res.strip().upper() == "S":
                print("Reiniciando o bot...")
                os.system("cls" if os.name == "nt" else "clear")
                os.system("python src/mello.py")
            elif res.strip().upper() == "E":
                print("Saindo do bot...")
                await bot.close()
            else:
                print("Ops! O bot não foi reiniciado, tente novamente.")
        except Exception as e:
            print(f"Erro {e}")
            await bot.close()
        break
    
@bot.command()
# ctx guarda o contexto da mensagem, processando o comando | tipamos o comando mello com o tipo commands.Context que é o tipo de dado que o discord.py espera
# o decorator @bot.command() transforma a função mello em um comando do bot
async def mello(ctx:commands.Context):
    nome = ctx.author.display_name
    await ctx.reply(f"Olá {nome} Como posso ajudar você?")
    
@bot.command()    
async def say(ctx:commands.Context, args):
    await ctx.send(args)
    
@bot.command()
async def some(ctx:commands.Context, num1:int, num2:int):
    resultado = num1 + num2
    await ctx.send(f"O resultado da soma é: {resultado}")
    
    
    
load_dotenv()
bot.run(os.getenv("TOKEN"))
