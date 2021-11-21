from logging import fatal
import discord
from discord import channel
from discord import embeds
from discord.embeds import Embed
import asyncio
from discord.ext import commands
import datetime
import time
import re
from discord import Webhook, RequestsWebhookAdapter, File


from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
from urllib import parse, request
from discord.ext.commands.bot import Bot
from discord.ext.commands.converter import EmojiConverter
from discord.ext.commands.core import command
from discord.utils import get
from discord import TextChannel
from youtube_dl import YoutubeDL
import json

from discord.ext.commands.errors import CheckAnyFailure

bot = commands.Bot(command_prefix='!', description="This is a Helper Bot")
bot.remove_command('help')

@bot.command()
async def ping(ctx):
    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"Pong!  `{int(ping)}ms`")

#CALCULATOR
@bot.command() 
async def add(ctx,a:float, b:float): 
    await ctx.send(f"{a} + {b} = {a+b}") #Adds A and B

@bot.command() 
async def sub(ctx,a:float,b:float): 
    await ctx.send(f"{a} - {b} = {a-b}") #Subtracts A and B

@bot.command() 
async def multi(ctx,a:int,b:int): 
    await ctx.send(f"{a} * {b} = {a*b}") #Multplies A and B

@bot.command() 
async def divide(ctx,a:int,b:int): 
    await ctx.send(f"{a} / {b} = {a/b}") #Divides A and B

@bot.command()
async def square(ctx,a:int):
    await ctx.send(f"{a*a}") #Multilies A by itself

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Board Exams | !help"))
    print('My Ready is Body.')

bot.run('ODM1MjA2MDg2NTcwODAzMjEx.YIMESA.kTDVUvg5x0sOPs4wOUCZYMPLojo')