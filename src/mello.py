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
        except ValueError:
            print(f"Erro")
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
async def calcule(ctx: commands.Context, expression: str):
    try:
        # avalia a expressão matemática de forma segura
        result = eval(expression, {"__builtins__": None}, {})
        await ctx.send(f"O resultado da operação '{expression}' é: {result}")
    except Exception as e:
        await ctx.send(f"Ops! Não consegui calcular a expressão. Verifique se está correta. Erro: {e}")
    
    
load_dotenv()
bot.run(os.getenv("TOKEN"))
