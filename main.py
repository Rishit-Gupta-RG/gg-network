import disnake
from disnake import AllowedMentions, Intents, Interaction, channel
from disnake import embeds
from disnake.embeds import Embed
import asyncio
from disnake.ext import commands
import datetime
import time
import os
import random
import re
from disnake import Member
from disnake.ext.commands import has_permissions, MissingPermissions
from urllib import parse, request
from disnake.ext.commands.bot import Bot
from disnake.ext.commands.converter import EmojiConverter
from disnake.ext.commands.core import command
from disnake.utils import get
from disnake import TextChannel
from disnake import ui
import sys, traceback
import json
from disnake import AppCommandInteraction
import aiohttp
from mcstatus import BedrockServer
from dotenv import load_dotenv
load_dotenv()
from disnake.ext import tasks
from disnake.ext.commands.errors import CheckAnyFailure

intents = disnake.Intents.default()
intents.presences = True
intents.members = True
intents.messages = True
bot = commands.Bot(command_prefix=commands.when_mentioned,test_guilds=[817003562663149578], intents=intents, case_insensitive=True)
disnake.AllowedMentions(users=False)

initial_extensions = ['cogs.minecraft', 'cogs.mod']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.command(hidden=True)
async def ping(ctx):
    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"Pong!  `{int(ping)}ms`")

class Refresh(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None,)
        self.value = None
    
    @disnake.ui.button(label="Refresh", style=disnake.ButtonStyle.blurple, emoji='🔃', custom_id='refbutton')
    async def confirm(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.send_message("Refreshing 🔃", ephemeral=True)
        self.value = True
        server = BedrockServer.lookup('ggnetworkk.aternos.me:34624')
        status = server.status()
        if status.players_max == 1:
            off = disnake.Embed(title="GG Network status panel.", description="**Status -** Offline :red_circle:\n\nDo you want to play now? Turn it on thorugh [Aternos Dashboard](https://aternos.org/server/) or ask someone with <@&880915882895872080> role to turn it on.", color=0xf80000)
            off.set_thumbnail(url="https://cdn.discordapp.com/icons/817003562663149578/a_427636e6c26d830bbcc36969a9e83608.gif?size=4096")
            off.set_author(icon_url="https://cdn.discordapp.com/icons/817003562663149578/a_427636e6c26d830bbcc36969a9e83608.gif?size=4096", name="ggnetworkk.aternos.me")
            off.set_footer(text='Click on the refresh button below to refresh the status.')
            await interaction.message.edit(embed=off)
        else:
            on = disnake.Embed(title="GG Network status panel.", description=f"**Status -** Online :green_circle:\n\n**Online Players-** `{status.players_online}`\n**Max. Players -** `{status.players_max}`\n**Ping -** `{int(status.latency*100)}ms`", color=0x3cff00)
            on.set_thumbnail(url="https://cdn.discordapp.com/icons/817003562663149578/a_427636e6c26d830bbcc36969a9e83608.gif?size=4096")
            on.set_footer(text='Click on the refresh button below to refresh the status.')
            on.set_author(icon_url="https://cdn.discordapp.com/icons/817003562663149578/a_427636e6c26d830bbcc36969a9e83608.gif?size=4096", name="ggnetworkk.aternos.me")
            await interaction.message.edit(embed=on)
    

@bot.command(hidden=True, description='deploys status checker.')
async def deploy(ctx):
    view = Refresh()
    off = disnake.Embed(title="Status for GG Network", description="Oh! no the server is offline \🔴\n\n Do you want to play now? Turn it on thorugh [Aternos Dashboard](https://aternos.org/server/) or ask someone with <@&880915882895872080> role to turn it on.", color=ctx.author.color)
    off.set_footer(icon_url=ctx.guild.icon, text=ctx.guild.name)
    await ctx.send(embed=off, view=view)

@bot.event
async def on_ready():
    print('Bot is ready.')
    bot.add_view(view=Refresh())

bot.run(os.getenv('TOKEN'))
