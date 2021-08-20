from logging import fatal
import discord
from discord import channel
from discord import embeds
from discord.embeds import Embed
from discord.ext import commands
import datetime
import time
import re

from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
from urllib import parse, request
from discord.ext.commands.bot import Bot
from discord.ext.commands.converter import EmojiConverter
from discord.ext.commands.core import command


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
async def add(ctx,a:int, b:int): 
    await ctx.send(f"{a} + {b} = {a+b}") #Adds A and B

@bot.command() 
async def sub(ctx,a:int,b:int): 
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

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="GG SMP BOT!", description="Hello, I am **GG SMP BOT** made for __GG SMP__ a Minecraft server \n" "Here's the list of available commands", color=discord.Color.purple())
    embed.add_field(name="Information:", value="`serverinfo`,`check`", inline=False)
    embed.add_field(name="Maths:", value="`add`, `sub`, `multi`, `divide`, `square`")
    embed.add_field(name='Other Commands', value="`youtube`", inline=False)
    embed.add_field(name="Moderation:", value="`kick`", inline=False)
    embed.add_field(name="Utilities:", value="`about`, `ping`", inline=False)
    
    embed.set_footer(text="My prefix in this guild !, More commands will be added soon ;)")
    await ctx.send(embed=embed)

@bot.command()
async def hhgg(ctx):
    embed = discord.Embed(title="SERVER RULES", color=discord.Color.blue())
    embed.add_field(name="Minecraft Server Rules", value="**1.** Don't steal anyone's item or opening someone chest without their permission is not allowed. \n""**2.** Be like a real warrior! Don't attack on someone without making them aware of it.\n""If you don't follow the above point and directly attack then its __responsibility of other players nearby to kill the player who is breaking this rule__.\n""**3.** If someone hits you by mistake then don't hit him back, this leads in a conflict.\n""**4.** Everyone have to contribute in public builds.\n""**5.** Do not damage property of others.\n""**6.** Mass use of **TNT** is strictly prohibited. Even in debris mining make sure you call a metting before going to mine debris with **TNT**.\n""**7.** Make sure you sleep when everyone is sleeping, if you are in a serious condition and can't sleep then leave the server and rejoin.", inline=False)
    embed.add_field(name="Discord Server Rules", value="There will be no rules in this discord server and no automod. But still don't break the basic rules.", inline=False)
    embed.add_field(name="SERVER INFO", value="**Server IP** - `RiAKG.aternos.me`\n""**Port** - `34624`\n", inline=False)
    embed.add_field(name="SERVER FAQ", value="You can't join server anytime, you can check if server is online or offline in <#859365811473874964>. If server is offline then you can ask <@&872499621149163620> to turn it back on.", inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def about(ctx):
    embed = discord.Embed(title="GG SMP", description= "Official Bot of GG SMP!", color=discord.Color.red())
    embed.add_field(name="**Developed by -**", value="Rishit Gupta")

    await ctx.send(embed=embed)

@bot.command()
async def serverinfo(ctx):
  name = str(ctx.guild.name)
  description = str(ctx.guild.description)

  owner = "**AKG#1234**"
  id = str(ctx.guild.id)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)

  icon = str(ctx.guild.icon_url)
   
  embed = discord.Embed(
      title=name + " Server Information",
      description=description,
      color=discord.Color.blue()
    )
  embed.set_thumbnail(url=icon)
  embed.add_field(name="Owner", value=owner, inline=True)
  embed.add_field(name="Server ID", value=id, inline=True)
  embed.add_field(name="Region", value=region, inline=True)
  embed.add_field(name="Member Count", value=memberCount, inline=True)

  await ctx.send(embed=embed)

@bot.command()
async def check(ctx):
    embed = discord.Embed(title="Checking Server Status", color=discord.Color.gold())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.add_field(name="To check status of the server :", value= " Go to <#859365811473874964> and react with :arrows_counterclockwise:\n" "**OR \n**" "Type `?check`.")

    await ctx.send(embed=embed)
    
@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_content= html_content.read().decode()
    search_results = re.findall(r'\/watch\?v=\w+', search_content)
    #print(search_results)
    await ctx.send("Here's what I found" ' ' 'https://www.youtube.com' + search_results[0])

#MODERATION
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member):
    await member.kick()
    await ctx.send(f"{member.name} has been kicked by {ctx.author.name}!")
async def kick_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await bot.send_message(ctx.message.channel, text)

#MUSIC SECTION %ARCHIEVED TILL LIBRARY IS INSTALLED%

#AUTO PLAYER HELP
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if not message.channel.id == 871006184990212118:
      return
    if "trade" or "trading" in message.content:
        embed = discord.Embed(title= "Trading", description="The [trading](https://minecraft.fandom.com/wiki/Trading#Bedrock_Edition_offers) system is a gameplay mechanic that allows players to trade emeralds for items and vice-versa with villagers as well as wandering traders.\n""**There are 5 Tiers of trading:**\n""1. Novice\n""2. Apprentice\n""3. Journeyman\n""4. Expert\n""5. Master", color=discord.Colour.blurple())
        embed.set_thumbnail('https://media.discordapp.net/attachments/868956059409203241/872541491061481482/AKG_Server_icon.gif')

        await message.channel.send(embed=embed)
        
#BOT ACTVITY STATUS
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Players in SMP | !help"))
    print('My Ready is Body')

bot.run('ODY0OTUzMzc5MjEzNjcyNDU4.YO88mw.TMzGde4mx5tItrZXwE9qIy8p-Vg')