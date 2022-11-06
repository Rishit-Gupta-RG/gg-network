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
from disnake.ext import tasks
from disnake.ext.commands.errors import CheckAnyFailure

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    ANIMALS = ["Panda", "Dog", "Cat", "Fox", "Red panda", "Koala", "Bird", "Racoon", "Kangaroo", "Whale", "Pikachu"]
    async def autocomp_animals(inter: disnake.ApplicationCommandInteraction, user_input: str):
        return [lang for lang in ANIMALS if user_input.lower() in lang]
    FACT_ANIMALS = ["Panda", "Dog", "Cat", "Fox", "Red panda", "Koala", "Bird", "Racoon", "Kangaroo", "Whale", "Pikachu"]
    async def autocomp_animalfact(inter: disnake.ApplicationCommandInteraction, user_input: str):
        return [lang for lang in FACT_ANIMALS if user_input.lower() in lang]

    @commands.slash_command()
    async def animal(self, inter):
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
        
    @commands.slash_command(description="Seaches on youtube for a given query.")
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

def setup(bot):
    bot.add_cog(Misc(bot))