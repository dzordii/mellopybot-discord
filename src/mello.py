import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from commands import util, logs, funny

intents = discord.Intents.all()
bot = commands.Bot("!", intents=intents)

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    try:
        await logs.setup(bot)
        await util.setup(bot)
        await funny.setup(bot)
        print("Comandos configurados com sucesso!")
    except Exception as e:
        print(f"Erro ao configurar comandos: {e}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} comandos de barra!")
    except Exception as e:
        print(f"Erro ao sincronizar comandos de barra: {e}")
    
    server = bot.get_guild(862163901281075200)
    if server:
        print(f"Bot conectado ao servidor: {server.name} (ID: {server.id})")
    else:
        print("O bot não está conectado ao servidor especificado.")
    print("O bot está pronto!")
    print(f"Nome do bot: {bot.user.name}")
    print(f"ID do bot: {bot.user.id}")

        
load_dotenv()
bot.run(os.getenv("TOKEN"))