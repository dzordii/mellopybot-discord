import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from commands import util, logs



# guardando permissões de intents
intents = discord.Intents.all()
bot = commands.Bot("", intents=intents)


@bot.event
async def on_ready():
    await bot.wait_until_ready()
    await bot.change_presence(activity=discord.Game(name="Mello - /mello"))
    await logs.setup(bot)
    await util.setup(bot) 
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} comandos de barra!")
    except Exception as e:
        print(f"Erro ao sincronizar comandos de barra: {e}")
    
    server = bot.get_guild(862163901281075200) # ID do servidor
    print("O bot está pronto!")
    print(f"Nome do bot: {bot.user.name}")
    print(f"ID do bot: {bot.user.id}")
    print(f"Bot conectado ao servidor {server}!")
    
    
load_dotenv()
bot.run(os.getenv("TOKEN"))
