from cgitb import text
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
import aiohttp
from psutil import users
from mcstatus import BedrockServer
from dotenv import load_dotenv
load_dotenv()

from disnake.ext.commands.errors import CheckAnyFailure
with open('config/config.json', 'r') as f:
    data = json.load(f)

intents = disnake.Intents.default()
intents.presences = True
intents.members = True
intents.messages = True
bot = commands.Bot(command_prefix=commands.when_mentioned,test_guilds=[817003562663149578], intents=intents, case_insensitive=True)
disnake.AllowedMentions(users=False)

initial_extensions = ['cogs.minecraft']

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
        server = BedrockServer.lookup(data["server_ip"])
        status = server.status()
        if status.players_max == 1:
            off = disnake.Embed(title="GG Network status panel.", description="**Status -** Offline :red_circle:\n\nDo you want to play now? Turn it on thorugh [Aternos Dashboard](https://aternos.org/server/) or ask someone with <@&880915882895872080> role to turn it on.", color=0xf80000)
            off.set_thumbnail(url="https://cdn.discordapp.com/icons/817003562663149578/a_427636e6c26d830bbcc36969a9e83608.gif?size=4096")
            off.set_author(icon_url="https://cdn.discordapp.com/icons/817003562663149578/a_427636e6c26d830bbcc36969a9e83608.gif?size=4096", name="ggnetworkk.aternos.me")
            off.set_footer(text='Click on the refresh button below to refresh the status.')
            await interaction.message.edit(embed=off)
        else:
            on = disnake.Embed(title="GG Network status panel.", description=f"**Status -** Online :green_circle:\n\n**Online Players-** `{status.players_online}`\n**Max. Players -** `{status.players_max}`\n**Edition -** "+data["minecraft_version"]+f"\n**Ping -** `{int(status.latency*100)}ms`", color=0x3cff00)
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

ANIMALS = ["Panda", "Dog", "Cat", "Fox", "Red panda", "Koala", "Bird", "Racoon", "Kangaroo", "Whale", "Pikachu"]
async def autocomp_animals(inter: disnake.ApplicationCommandInteraction, user_input: str):
    return [lang for lang in ANIMALS if user_input.lower() in lang]
FACT_ANIMALS = ["Panda", "Dog", "Cat", "Fox", "Red panda", "Koala", "Bird", "Racoon", "Kangaroo", "Whale", "Pikachu"]
async def autocomp_animalfact(inter: disnake.ApplicationCommandInteraction, user_input: str):
    return [lang for lang in FACT_ANIMALS if user_input.lower() in lang]

@bot.slash_command()
async def animal(inter):
    pass

@animal.sub_command(description="Sends a picture of selected animal.")
async def image(inter: disnake.ApplicationCommandInteraction, animal: str = commands.Param(autocomplete=autocomp_animals)):
    """
    Sends a picture of selected animal.
    
    Parameters
    ----------
    animal: Select an animal to see its picture.
    """
    if animal in ("Panda", "Dog", "Cat", "Fox","Koala", "Bird", "Racoon", "Kangaroo", "Whale", "Pikachu"):
        k = animal.lower()
        async with aiohttp.ClientSession() as session:
            request = await session.get(f'https://some-random-api.ml/img/{k}')
            whalejson = await request.json()
        embed = disnake.Embed(title=f"{animal}!", color=inter.author.color)
        embed.set_image(url=whalejson['link'])
        await inter.response.send_message(embed=embed)
    else:
        async with aiohttp.ClientSession() as session:
            request = await session.get(f'https://some-random-api.ml/img/red_panda')
            whalejson = await request.json()
        embed = disnake.Embed(title=f"{animal}!", color=inter.author.color)
        embed.set_image(url=whalejson['link'])
        await inter.response.send_message(embed=embed)

@bot.command()
async def btest(ctx):
    with open ('banner/nice.gif', 'rb') as f:
        await ctx.guild.edit(banner=f.read())

@animal.sub_command(description="Sends a random fact of selected animal.")
async def fact(inter: disnake.ApplicationCommandInteraction, animal: str = commands.Param(autocomplete=autocomp_animalfact)):
    """
    Sends a random fact of selected animal.
    
    Parameters
    ----------
    animal: Select an animal to see its fact.
    """
    if animal in ("Panda", "Dog", "Cat", "Fox","Koala", "Bird", "Racoon", "Kangaroo", "Whale"):
        k = animal.lower()
        async with aiohttp.ClientSession() as session:
            request = await session.get(f'https://some-random-api.ml/facts/{k}')
            whalejson = await request.json()
        embed = disnake.Embed(title=f"{animal} Fact!",description=whalejson['fact'],color=inter.author.color)
        await inter.response.send_message(embed=embed)
    else:
        async with aiohttp.ClientSession() as session:
            request = await session.get(f'https://some-random-api.ml/facts/red_panda')
            whalejson = await request.json()
        embed = disnake.Embed(title=f"{animal} Fact!",description=whalejson['fact'],color=inter.author.color)
        await inter.response.send_message(embed=embed)
    
@bot.slash_command(description="Seaches on youtube for a given query.")
async def youtube(ctx, *, search):
    """
    Seaches on youtube for a given query.
    
    Parameters
    ----------
    search: The query to search for
    """
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_content= html_content.read().decode()
    search_results = re.findall(r'\/watch\?v=\w+', search_content)
    await ctx.send("Here's what I found" ' ' 'https://www.youtube.com' + search_results[0])

@bot.event
async def on_ready():
    print('Bot is ready.')
    bot.add_view(view=Refresh())

bot.run(os.getenv('TOKEN'))
