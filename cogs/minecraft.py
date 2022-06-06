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

class Minecraft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command(description="Checks status for GG Network.")
    async def check(self, ctx):
        server = BedrockServer.lookup('ggnetworkk.aternos.me:34624')
        status = server.status()
        if status.players_max == 1:
            off = disnake.Embed(title="Status for GG Network", description="Oh! no the server is offline \🔴\n\n Do you want to play now? Turn it on thorugh [Aternos Dashboard](https://aternos.org/server/) or ask someone with <@&880915882895872080> role to turn it on.", color=0xf80000, timestamp=datetime.utcnow())
            off.set_footer(icon_url=ctx.guild.icon, text=ctx.guild.name)
            await ctx.send(embed=off)
        else:
            on = disnake.Embed(title="Status for GG Network", description=f"**Status -** Online \🟢\n**Online players -** `{status.players_online}`\n**Ping -** `{int(status.latency*100)}ms`", color=0x3cff00, timestamp=datetime.utcnow())
            on.set_footer(icon_url=ctx.guild.icon, text=ctx.guild.name)
            on.set_author(name="ggnetworkk.aternos.me")
            on.set_thumbnail(url=ctx.guild.icon)
            await ctx.send(embed=on)


def setup(bot):
    bot.add_cog(Minecraft(bot))
