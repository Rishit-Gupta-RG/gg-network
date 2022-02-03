from logging import fatal
import disnake
from disnake import Intents, channel
from disnake import embeds
from disnake.embeds import Embed
import asyncio
from disnake.ext import commands
import datetime
import time
import re
from disnake import Member
from disnake.ext.commands import has_permissions, MissingPermissions
from urllib import parse, request
from disnake.ext.commands.bot import Bot
from disnake.ext.commands.converter import EmojiConverter
from disnake.ext.commands.core import command
from disnake.utils import get
from disnake import TextChannel
import json

from disnake.ext.commands.errors import CheckAnyFailure

intents = disnake.Intents.default()
intents.presences = True
intents.members = True
bot = commands.InteractionBot(test_guilds=[817003562663149578], intents=intents)
bot.remove_command('help')

@bot.slash_command()
async def ping(ctx):
    before = time.monotonic()
    ping = (time.monotonic() - before) * 1000
    await ctx.send(f"Pong!  `{int(ping)}ms`")

#CALCULATOR
@bot.slash_command() 
async def add(ctx,a:float, b:float): 
    await ctx.send(f"{a} + {b} = {a+b}") #Adds A and B

@bot.slash_command() 
async def sub(ctx,a:float,b:float): 
    await ctx.send(f"{a} - {b} = {a-b}") #Subtracts A and B

@bot.slash_command() 
async def multi(ctx,a:int,b:int): 
    await ctx.send(f"{a} * {b} = {a*b}") #Multplies A and B

@bot.slash_command() 
async def divide(ctx,a:int,b:int): 
    await ctx.send(f"{a} / {b} = {a/b}") #Divides A and B

@bot.slash_command()
async def square(ctx,a:int):
    await ctx.send(f"{a*a}") #Multilies A by itself


@bot.slash_command()
async def help(ctx):
    embed = disnake.Embed(title="GG SMP BOT!", description="Hello, I am **GG SMP BOT** made for __GG SMP__ a Minecraft server \n" "Here's the list of available commands", color=disnake.Color.purple())
    embed.add_field(name="Information:", value="`serverinfo`,`check`", inline=False)
    embed.add_field(name="Maths:", value="`add`, `sub`, `multi`, `divide`, `square`")
    embed.add_field(name='Other Commands', value="`youtube`", inline=False)
    embed.add_field(name="Moderation:", value="`kick`", inline=False)
    embed.add_field(name="Utilities:", value="`about`, `ping`", inline=False)
    
    embed.set_footer(text="My prefix in this guild !, More commands will be added soon ;)")

    await ctx.send(embed=embed)

@bot.slash_command()
async def hhgg(ctx):
    embed = disnake.Embed(title="SERVER RULES", color=disnake.Color.blue())
    embed.add_field(name="Minecraft Server Rules", value="**1.** Don't steal anyone's item or opening someone chest without their permission is not allowed. \n""**2.** Be like a real warrior! Don't attack on someone without making them aware of it.\n""If you don't follow the above point and directly attack then its __responsibility of other players nearby to kill the player who is breaking this rule__.\n""**3.** If someone hits you by mistake then don't hit him back, this leads in a conflict.\n""**4.** Everyone have to contribute in public builds.\n""**5.** Do not damage property of others.\n""**6.** Mass use of **TNT** is strictly prohibited. Even in debris mining make sure you call a metting before going to mine debris with **TNT**.\n""**7.** Make sure you sleep when everyone is sleeping, if you are in a serious condition and can't sleep then leave the server and rejoin.", inline=False)
    embed.add_field(name="Disnakedisnake Server Rules", value="There will be no rules in this disnake server and no automod. But still don't break the basic rules.", inline=False)
    embed.add_field(name="SERVER INFO", value="**Server IP** - `RiAKG.aternos.me`\n""**Port** - `34624`\n", inline=False)
    embed.add_field(name="SERVER FAQ", value="Server is not online for 24/7, You can check staus of server by typing `!check`. If server is offline then you can ask <@&880915882895872080> to turn it back on.", inline=False)

    await ctx.send(embed=embed)

@bot.slash_command()
async def about(ctx):
    embed = disnake.Embed(title="GG SMP", description= "Official Bot of GG SMP!", color=disnake.Color.red())
    embed.add_field(name="**Developed by -**", value="Rishit Gupta")

    await ctx.send(embed=embed)

@bot.slash_command()
async def serverinfo(ctx):
  name = str(ctx.guild.name)
  description = str(ctx.guild.description)

  owner = "**AKG#1234**"
  id = str(ctx.guild.id)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)

  icon = str(ctx.guild.icon_url)
   
  embed = disnake.Embed(
      title=name + " Server Information",
      description=description,
      color=disnake.Color.blue()
    )
  embed.set_thumbnail(url=icon)
  embed.add_field(name="Owner", value=owner, inline=True)
  embed.add_field(name="Server ID", value=id, inline=True)
  embed.add_field(name="Region", value=region, inline=True)
  embed.add_field(name="Member Count", value=memberCount, inline=True)

  await ctx.send(embed=embed)

    
@bot.slash_command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_content= html_content.read().decode()
    search_results = re.findall(r'\/watch\?v=\w+', search_content)
    #print(search_results)
    await ctx.send("Here's what I found" ' ' 'https://www.youtube.com' + search_results[0])


#MODERATION
@bot.slash_command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: disnake.Member):
    await member.kick()
    await ctx.send(f"**{member.name}** has been kicked by **{ctx.author.name}**!")
async def kick_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await bot.send_message(ctx.message.channel, text)

#MUSIC

# players = {}
# # command to play sound from a youtube URL
# @bot.command()
# async def play(ctx, url):
#     YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
#     FFMPEG_OPTIONS = {
#         'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
#     voice = get(bot.voice_clients, guild=ctx.guild)

#     if voice is not None and not voice.is_playing():
#         with YoutubeDL(YDL_OPTIONS) as ydl:
#             info = ydl.extract_info(url, download=False)
#         URL = info['url']
#         voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
#         voice.is_playing()
#         await ctx.send('Bot is playing')

# # check if the bot is already playing
#     else:
#         await ctx.send("Bot is already playing")
#         return


# # command to resume voice if it is paused
# @bot.command()
# async def resume(ctx):
#     voice = get(bot.voice_clients, guild=ctx.guild)

#     if not voice.is_playing():
#         voice.resume()
#         await ctx.send('Bot is resuming')


# # command to pause voice if it is playing
# @bot.command()
# async def pause(ctx):
#     voice = get(bot.voice_clients, guild=ctx.guild)

#     if voice.is_playing():
#         voice.pause()
#         await ctx.send('Bot has been paused')


## command to stop voice
#  @bot.command()
# async def stop(ctx):
#     voice = get(bot.voice_clients, guild=ctx.guild)

#     if voice.is_playing():
#         voice.stop()
#         await ctx.send('Stopping...')
 
#BOT ACTVITY STATUS
@bot.event
async def on_ready():
    print('GG is read.')

bot.run('ODY0OTUzMzc5MjEzNjcyNDU4.YO88mw.TMzGde4mx5tItrZXwE9qIy8p-Vg')