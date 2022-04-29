from cgitb import text
from unicodedata import name
import disnake
from disnake.ext import commands
from disnake import AllowedMentions, member, channel
from psutil import users
import random
import json

class Minecraft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    ANIMALS = ["panda", "dog", "cat", "fox", "red panda", "koala", "bird", "racoon", "kangaroo", "whale", "pikachu"]
    async def autocomp_animals(inter: disnake.ApplicationCommandInteraction, user_input: str):
        return [lang for lang in ANIMALS if user_input.lower() in lang]

    
    @commands.slash_command()
    async def animal(inter):
        pass

    @animal.sub_command()
    async def image(inter: disnake.ApplicationCommandInteraction, animal: str = commands.Param(autocomplete=autocomp_animals)):
        


def setup(bot):
    bot.add_cog(Minecraft(bot))