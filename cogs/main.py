from logging import fatal
from socket import CAN_BCM_TX_ANNOUNCE
import disnake
from disnake import AllowedMentions, Intents, Interaction, channel
from disnake import embeds
from disnake.embeds import Embed
import asyncio
from disnake.ext import commands
import datetime
import time
import os
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

from psutil import users
from mcstatus import MinecraftBedrockServer
from dotenv import load_dotenv
load_dotenv()

from disnake.ext.commands.errors import CheckAnyFailure

intents = disnake.Intents.default()
intents.presences = True
intents.members = True
intents.messages = True
bot = commands.Bot(command_prefix="!",test_guilds=[817003562663149578], intents=intents, case_insensitive=True)
disnake.AllowedMentions(users=False)

initial_extensions = ['cogs.moderation', 'cogs.minecraft', 'cogs.roles']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.command()
async def ping(ctx):
    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"Pong!  `{int(ping)}ms`")

class Refresh(disnake.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
        self.inter = Interaction
    
    @disnake.ui.button(label="Refresh", style=disnake.ButtonStyle.green, emoji='🔃')
    async def confirm(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.send_message("Refreshing", ephemeral=True)
        self.value = True
        self.stop()
server = BedrockServer.lookup("ggnetworkk.aternos.me:34624")
status = server.status()

@bot.command(hidden=True, description='deploys status checker.')
async def deploy(ctx):
    view = Refresh()
    off = disnake.Embed(title="Status for GG Network", description="Oh! no the server is offline \🔴\n\n Do you want to play now? Turn it on thorugh [Aternos Dashboard](https://aternos.org/server/) or ask someone with <@&880915882895872080> role to turn it on.", color=ctx.author.color)
    off.set_footer(icon_url=ctx.guild.icon, text=ctx.guild.name)
    msg = await ctx.send(embed=off, view=view)
    await view.wait()
    if status.players_max == "1":
        await msg.edit_original_message(embed=off)
    else:
        await msg.edit_original_message("Server is on.")
    

# @bot.slash_command(description="About me.")
# async def about(ctx):
#     embed = disnake.Embed(title="GG SMP", description= "Official Bot of GG SMP!", color=disnake.Color.red())
#     embed.add_field(name="**Developed by -**", value="Rishit Gupta")

#     await ctx.send(embed=embed)

# @bot.slash_command(description="Shows server information.")
# async def serverinfo(ctx):
#   name = str(ctx.guild.name)
#   description = str(ctx.guild.description)

#   owner = "**AKG#1234**"
#   id = str(ctx.guild.id)
#   region = str(ctx.guild.region)
#   memberCount = str(ctx.guild.member_count)

#   icon = str(ctx.guild.icon_url)
   
#   embed = disnake.Embed(
#       title=name + " Server Information",
#       description=description,
#       color=disnake.Color.blue()
#     )
#   embed.set_thumbnail(url=icon)
#   embed.add_field(name="Owner", value=owner, inline=True)
#   embed.add_field(name="Server ID", value=id, inline=True)
#   embed.add_field(name="Region", value=region, inline=True)
#   embed.add_field(name="Member Count", value=memberCount, inline=True)

#   await ctx.send(embed=embed)

    
@bot.slash_command(description="Seached on youtube for a given query.")
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_content= html_content.read().decode()
    search_results = re.findall(r'\/watch\?v=\w+', search_content)
    await ctx.send("Here's what I found" ' ' 'https://www.youtube.com' + search_results[0])

@bot.event
async def on_ready():
    print('GG is ready.')

bot.run(os.getenv('TOKEN'))
