import discord
from discord import app_commands
from discord.ext import commands

log_channels = {}

async def setup(bot: commands.Bot):
    @bot.tree.command(name="logs", description="Configura o canal de logs do servidor")
    @app_commands.describe(canal="Escolha o canal onde os logs serão enviados")
    @app_commands.checks.has_permissions(administrator=True)
    async def logs(interaction: discord.Interaction, canal: discord.TextChannel):
        log_channels[interaction.guild.id] = canal.id
        embed = discord.Embed(
            title="Canal de Logs Configurado",
            description=f"Todos os logs serão enviados para {canal.mention}",
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed)

    @logs.error
    async def logs_error(interaction: discord.Interaction, error):
        if isinstance(error, app_commands.MissingPermissions):
            await interaction.response.send_message("Você precisa ser administrador para usar esse comando.", ephemeral=True)
        else:
            await interaction.response.send_message("Ocorreu um erro ao definir o canal de logs.", ephemeral=True)

    setup_events(bot)

def setup_events(bot: commands.Bot):
    async def send_log(guild_id, embed):
        canal_id = log_channels.get(guild_id)
        if canal_id is None:
            return
        canal_log = bot.get_channel(canal_id)
        if canal_log is None:
            return
        await canal_log.send(embed=embed)

    @bot.event
    async def on_message(message: discord.Message):
        if message.guild is None or message.author.bot:
            return
        embed = discord.Embed(
            title="💬 Mensagem Enviada",
            description=f"**Autor:** {message.author.mention}\n**Canal:** {message.channel.mention}",
            color=discord.Color.green()
        )
        embed.add_field(name="Conteúdo", value=message.content or "(sem texto)", inline=False)
        embed.set_footer(text=f"ID do autor: {message.author.id}")
        await send_log(message.guild.id, embed)

    @bot.event
    async def on_message_delete(message: discord.Message):
        if message.guild is None or message.author.bot:
            return
        embed = discord.Embed(
            title="🗑️ Mensagem Deletada",
            description=f"**Autor:** {message.author.mention}\n**Canal:** {message.channel.mention}",
            color=discord.Color.red()
        )
        embed.add_field(name="Conteúdo", value=message.content or "(sem texto)", inline=False)
        embed.set_footer(text=f"ID do autor: {message.author.id}")
        await send_log(message.guild.id, embed)

    @bot.event
    async def on_message_edit(before: discord.Message, after: discord.Message):
        if before.guild is None or before.author.bot:
            return
        embed = discord.Embed(
            title="✏️ Mensagem Editada",
            description=f"**Autor:** {before.author.mention}\n**Canal:** {before.channel.mention}",
            color=discord.Color.blue()
        )
        embed.add_field(name="Antes", value=before.content or "(sem texto)", inline=False)
        embed.add_field(name="Depois", value=after.content or "(sem texto)", inline=False)
        embed.set_footer(text=f"ID do autor: {before.author.id}")
        await send_log(before.guild.id, embed)

    @bot.event
    async def on_member_join(member: discord.Member):
        embed = discord.Embed(
            title="👋 Membro Entrou",
            description=f"{member.mention} entrou no servidor!",
            color=discord.Color.green()
        )
        embed.set_footer(text=f"ID do membro: {member.id}")
        await send_log(member.guild.id, embed)

    @bot.event
    async def on_member_remove(member: discord.Member):
        embed = discord.Embed(
            title="👋 Membro Saiu",
            description=f"{member.mention} saiu do servidor!",
            color=discord.Color.red()
        )
        embed.set_footer(text=f"ID do membro: {member.id}")
        await send_log(member.guild.id, embed)

    @bot.event
    async def on_guild_channel_create(channel: discord.abc.GuildChannel):
        embed = discord.Embed(
            title="📦 Canal Criado",
            description=f"Canal {channel.mention} foi criado!",
            color=discord.Color.green()
        )
        embed.set_footer(text=f"ID do canal: {channel.id}")
        await send_log(channel.guild.id, embed)

    @bot.event
    async def on_guild_channel_delete(channel: discord.abc.GuildChannel):
        embed = discord.Embed(
            title="📦 Canal Deletado",
            description=f"Canal {channel.name} foi deletado!",
            color=discord.Color.red()
        )
        embed.set_footer(text=f"ID do canal: {channel.id}")
        await send_log(channel.guild.id, embed)

    @bot.event
    async def on_guild_channel_update(before: discord.abc.GuildChannel, after: discord.abc.GuildChannel):
        embed = discord.Embed(
            title="🔄 Canal Atualizado",
            description=f"Atualizações para {before.mention}",
            color=discord.Color.orange()
        )
        if before.name != after.name:
            embed.add_field(name="Nome", value=f"Antes: {before.name}\nDepois: {after.name}", inline=False)
        embed.set_footer(text=f"ID do canal: {before.id}")
        await send_log(before.guild.id, embed)

    @bot.event
    async def on_guild_update(before: discord.Guild, after: discord.Guild):
        embed = discord.Embed(
            title="🔄 Servidor Atualizado",
            description=f"Atualizações para {before.name}",
            color=discord.Color.orange()
        )
        if before.name != after.name:
            embed.add_field(name="Nome", value=f"Antes: {before.name}\nDepois: {after.name}", inline=False)
        embed.set_footer(text=f"ID do servidor: {before.id}")
        await send_log(before.id, embed)

    @bot.event
    async def on_member_update(before: discord.Member, after: discord.Member):
        embed = discord.Embed(
            title="🔄 Membro Atualizado",
            description=f"Atualizações para {before.mention}",
            color=discord.Color.orange()
        )
        if before.nick != after.nick:
            embed.add_field(name="Apelido", value=f"Antes: {before.nick}\nDepois: {after.nick}", inline=False)
        embed.set_footer(text=f"ID do membro: {before.id}")
        await send_log(before.guild.id, embed)
