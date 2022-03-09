from datetime import datetime
from sqlite3 import Timestamp
from unicodedata import name
from mcstatus import MinecraftBedrockServer
import disnake
from disnake.ext import commands
from disnake import AllowedMentions, member, channel
from psutil import users
import random

class Minecraft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="check", description="Checks status for GG Network", breif="Want to check whether the server is online or not? just type the command an you'll get some information.", enabled=True)
    async def check(self, ctx):
        server = MinecraftBedrockServer.lookup("ggnetworkk.aternos.me:34624")
        status = server.status()
        if status.players_max == '1':
            off = disnake.Embed(title="Status for GG Network", description="Oh! no the server is offline \🔴\n\n Do you want to play now? Turn it thorugh [Aternos Dashboard](https://aternos.org/server/) or ask someone with <@&880915882895872080> role to turn it on.", color=ctx.author.color, timestamp=datetime.datetime.utcnow())
            off.set_footer(icon_url=ctx.guild.icon, text=ctx.guild.name)
            await ctx.send(embed=off)
        else:
            on = disnake.Embed(name="Status for GG Network", description=f"**Edition -** Bedrock:1.18.2\n**IP -** `ggnetworkk.aternos.me`\n**Port -** `34624`\n**Status -** Online \🟢\n**Online players -** `{status.players_online}`\n**Ping -** `{int(status.latency*100)}`", color=ctx.author.color, timestamp=datetime.datetime.utcnow())
            on.set_footer(icon_url=ctx.guild.icon, text=ctx.guild.name)
            on.set_thumbnail(url=ctx.guild.icon)
            await ctx.send(embed=on)


def setup(bot):
    bot.add_cog(Minecraft(bot))