import discord
from discord.ext import commands
from discord import app_commands
import random

intents = discord.Intents.all()
bot = commands.Bot("", intents=intents)

async def setup(bot: commands.Bot):
    @bot.tree.command(name="coinflip", description="Cara ou Coroa")
    async def coinflip(interaction: discord.Interaction):
        result = random.choice(["Cara", "Coroa"])
        embed = discord.Embed(
            title="Resultado do Lançamento",
            description=f"O resultado é: {result}",
            color=discord.Color.gold()
        )
        await interaction.response.send_message(embed=embed)
        
    @bot.tree.command(name="diceroll", description="Lançar um dado")
    async def dice_roll(interaction: discord.Interaction, sides: int):
        result = random.randint(1, sides)
        embed = discord.Embed(
            title="Resultado do Lançamento",
            description=f"O resultado é: {result}",
            color=discord.Color.gold()
        )
        await interaction.response.send_message(embed=embed)
    
    @bot.tree.command(name="ppt", description="Jogar Pedra, Papel e Tesoura")
    async def rock_paper_scissors(interaction: discord.Interaction, choice: str):
        choices = ["Pedra", "Papel", "Tesoura"].lower()
        bot_choice = random.choice(choices)
        if choice == bot_choice:
            result = "Empate!"
        elif (choice == "pedra" and bot_choice == "tesoura") or (choice == "papel" and bot_choice == "pedra") or (choice == "tesoura" and bot_choice == "papel"):
            result = "Você venceu!"
        else:
            result = "Você perdeu!"
        
        embed = discord.Embed(
            title="Resultado do Jogo",
            description=f"Você escolheu: {choice}\nBot escolheu: {bot_choice}\nResultado: {result}",
            color=discord.Color.gold()
        )
        await interaction.response.send_message(embed=embed)
    
    @bot.tree.command(name="shipp", description="Shipar dois usuários")
    async def ship(interaction: discord.Interaction, user1: discord.User, user2: discord.User):
        if user1 == user2:
            result = "Você não pode shipar a si mesmo!"
        else:
            percentage = random.randint(0, 100)
            result = f"{user1.mention} e {user2.mention} têm {percentage}% de compatibilidade!"
        
        embed = discord.Embed(
            title="Resultado do Ship",
            description=result,
            color=discord.Color.gold()
        )
        await interaction.response.send_message(embed=embed)