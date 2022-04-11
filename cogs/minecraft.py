from datetime import datetime
from sqlite3 import Timestamp
from unicodedata import name
from mcstatus import BedrockServer
import disnake
from disnake.ext import commands
from disnake import AllowedMentions, member, channel
from psutil import users
import random
import json
with open('config/config.json', 'r') as f:
    data = json.loads(f)

class Minecraft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="check", brief="Checks status for GG Network", help="Want to check whether the server is online or not? just type the command an you'll get some information.", enabled=True)
    async def check(self, ctx):
        server = BedrockServer.lookup(data["server_ip"])
        status = server.status()
        if status.players_max == 1:
            off = disnake.Embed(title="Status for GG Network", description="Oh! no the server is offline \🔴\n\n Do you want to play now? Turn it on thorugh [Aternos Dashboard](https://aternos.org/server/) or ask someone with <@"+data["minecraft_admin_role_id"]+"> role to turn it on.", color=ctx.author.color, timestamp=datetime.utcnow())
            off.set_footer(icon_url=ctx.guild.icon, text=ctx.guild.name)
            await ctx.send(embed=off)
        else:
            on = disnake.Embed(title="Status for"+data["minecraft_server_name"], description=f"**Status -** Online \🟢\n**Online players -** `{status.players_online}`\n**Ping -** `{int(status.latency*100)}ms`", color=ctx.author.color, timestamp=datetime.utcnow())
            on.set_footer(icon_url=ctx.guild.icon, text=ctx.guild.name)
            on.set_author(name=data["server_ip"])
            on.set_thumbnail(url=ctx.guild.icon)
            await ctx.send(embed=on)


def setup(bot):
    bot.add_cog(Minecraft(bot))