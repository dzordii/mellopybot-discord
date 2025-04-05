import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot("", intents=intents)


async def setup(bot: commands.Bot):
    @bot.tree.command(name="mello", description="Comando de ajuda")
    async def mello(interaction: discord.Interaction):
        embed = discord.Embed(title="Comandos do Bot", description="Aqui estão os comandos disponíveis:")
        embed.add_field(name="/mello", value="Comando de ajuda", inline=False)
        embed.add_field(name="/say", value="Fala algo em nome do bot", inline=False)
        embed.add_field(name="/ping", value="Comando de ping", inline=False)
        await interaction.response.send_message(embed=embed)
        

    @bot.tree.command(name="say", description="Fala algo em nome do bot")
    async def say(interaction: discord.Interaction, message: str):
        await interaction.response.send_message(message)


    @bot.tree.command(name="ping", description="Comando de ping")
    async def ping(interaction: discord.Interaction):
        await interaction.response.send_message(f"Pong, Latencia: {round(bot.latency * 1000)}ms")
    