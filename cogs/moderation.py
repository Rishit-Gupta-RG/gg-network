from cgitb import text
from unicodedata import name
import disnake
from disnake.ext import commands
from disnake import AllowedMentions, member
from psutil import users

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        disnake.AllowedMentions(users=False)
    @commands.command(name="kick", description="Kicks a member.", help="Kicks a member from the server, you can also set a reason which will show in audit logs.", brief="Kicks a member.", usage="Usage:\n!kick <member> [reason]\n\nExamples:\n!k @Ronit badmosi\n !kick @Dyno", aliases=['k'], enabled=True)
    @commands.check_any(commands.has_role(930527570800287804), commands.is_owner(), commands.has_permissions(kick_members=True), commands.has_permissions(administrator=True))
    async def my_kick_command(self, ctx, member: disnake.Member, reason: str=None) -> None:
        dm = await member.create_dm()
        embed = disnake.Embed(title="Kick", description=f"<:_:949659326769950760> **{member.name}#{member.discriminator}** has been kicked susscessfully.", color=ctx.author.color)
        embed.set_author(url=ctx.author.display_avatar.url, name=ctx.author.name)
        embed.set_footer(icon_url=member.display_avatar.url, text=f"Reason - {reason}")
        await dm.send(f"You were kicked in **{ctx.guild.name}** by **{ctx.author.name}**.\n Reason - {reason}")
        await member.kick(reason=reason)
        await ctx.send(embed=embed)

    @commands.command(name="warn", brief="Warns a member.", description="Warns of member.", aliases=['w', 'warning'], usage='Usage:\n!warn <member> [reason]\nExamples:\n!warn @Arpit chat in off-topic channel.', enabled=True)
    @commands.check_any(commands.has_role(930527570800287804), commands.is_owner(), commands.has_permissions(kick_members=True), commands.has_permissions(administrator=True))
    async def my_warn_command(self, ctx, member: disnake.Member, reason: str):
        if reason == None:
            await ctx.send("<:_:949659578365251654> You need to provide a reason!")
        else:
            dm = await member.create_dm()
            embed = disnake.Embed(title="Warn", description=f"<:_:949659326769950760> **{member.name}#{member.discriminator}** has been warned.", color=ctx.author.color)
            embed.set_author(name=ctx.author.name, url=ctx.author.display_avatar.url)
            embed.set_footer(icon_url=member.display_avatar.url, text=f'Reason - {reason}')
            await dm.send(f"You recieved a warning in **{ctx.guild.name}** by **{ctx.author.name}**.\n Reason - {reason}")
            await ctx.send(embed=embed)

    @commands.command(name="timeout", description="Timeouts a member.", help="Timeouts a member in the server, you can also set a reason which will show in audit logs.", brief="Timeouts a member.", usage="Usage:\n!timeout <member> <duration> [reason]\n\nExamples:\n!timeout @Ronit 10m posting cringe\n !timeout @Sanskar 10h", aliases=['mute', 'to'], enabled=True)
    @commands.check_any(commands.has_role(930527570800287804), commands.is_owner(), commands.has_permissions(kick_members=True), commands.has_permissions(administrator=True))
    async def my_timeout_command(self, ctx, member: disnake.Member, duration,reason: str=None) -> None:
        time_convert = {'s': 1 , 'm' : 60 , 'h' : 3600 , 'd' : 86400, 'S' : 1, 'M' : 60, 'H' : 3600, "D" : 86400}
        timeout_time = float(duration[0:len(duration)-1]) * time_convert[duration[-1]]
        dm = await member.create_dm()
        embed = disnake.Embed(title="Timeout", description=f"<:_:949659326769950760> **{member.name}#{member.discriminator}** has been timed out susscessfully for **{duration}**.", color=ctx.author.color)
        embed.set_author(url=ctx.author.display_avatar.url, name=ctx.author.name)
        embed.set_footer(icon_url=member.display_avatar.url, text=f"Reason - {reason}")
        await dm.send(f"You were Timed out in **{ctx.guild.name}** by **{ctx.author.name}** for **{duration}**.\n Reason - {reason}")
        await member.timeout(reason=reason, duration=timeout_time)
        await ctx.send(embed=embed)

    @commands.command(name="ban", description="Bans a member.", help="Bans a member from the server, you can also set a reason which will show in audit logs.", brief="bans a member.", usage="Usage:\n!ban <member> [reason]\n\nExamples:\n!ban @Arnav anime is cringe\n !ban @carl-bot", aliases=['b'], enabled=True)
    @commands.check_any(commands.has_role(930527570800287804), commands.is_owner(), commands.has_permissions(kick_members=True), commands.has_permissions(administrator=True))
    async def my_ban_command(self, ctx, member: disnake.Member, reason: str=None) -> None:
        dm = await member.create_dm()
        embed = disnake.Embed(title="Ban", description=f"<:_:949659326769950760> **{member.name}#{member.discriminator}** was banned.", color=ctx.author.color)
        embed.set_author(url=ctx.author.display_avatar.url, name=ctx.author.name)
        embed.set_footer(icon_url=member.display_avatar.url, text=f"Reason - {reason}")
        await dm.send(f"You were banned from **{ctx.guild.name}** by **{ctx.author.name}**.\n Reason - {reason}")
        await member.ban(reason=reason)
        await ctx.send(embed=embed)
    
    @commands.command(name="nick", description="Changes nickname of a member.", brief="Changes nickname", usage="Usage:\n!nick <member> [new_nick]\n\nExamples:\n!sn @Ronit Badmas Gaymer", aliases=['sn', 'setnick', 'nickname'], enabled=True)
    @commands.check_any(commands.has_role(930527570800287804), commands.is_owner(), commands.has_permissions(kick_members=True), commands.has_permissions(administrator=True))
    async def my_nick_cmd(self, ctx, member: disnake.Member, new_nick: str):
        await member.edit(nick=new_nick)
        await ctx.send(f"<:_:949659326769950760> Changed nickname for {member}", allowed_mentions=users)


def setup(bot):
    bot.add_cog(Moderation(bot))