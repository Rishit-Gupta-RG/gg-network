from enum import unique
from pickle import PicklingError
from turtle import title
from typing_extensions import Self
import disnake
from disnake.ext import commands
from disnake import AllowedMentions, member, channel, role, guild, embeds

class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.group(case_insensitive=True)
    async def role(self, ctx):
        embed = disnake.embed(title='List of color roles.', description='Red\nGreen\nYellow\nBlue\nCyan\nPurple\nPink\nOrange\mBlack\nLime', color=ctx.author.color)
        await ctx.send(embed=embed)
    @commands.role.command(name='red')
    async def red(self, ctx):
        yellow = self.bot.get_role(858720010503192576)
        blue = self.bot.get_role(858720201709584425)
        red = self.bot.get_role(858719656990212117)
        green = self.bot.get_role(858720613585780736)
        cyan = self.bot.get_role(858720130964127756)
        pink = self.bot.get_role(858720420412784670)
        black = self.bot.get_role(858720473305972767)
        lime = self.bot.get_role(858720267019091998)
        purple = self.bot.get_role(858720793885540362)
        orange = self.bot.get_role(858720350303682571)
        if ctx.author.roles in (yellow, blue, green, cyan, pink, black, lime, purple, orange):
            await ctx.author.remove_roles(yellow, blue, green, cyan, pink, black, lime, purple, orange)
            await ctx.author.add_roles(red)
            await ctx.send('<:tick:949659326769950760> Updated your color to red.')
        
def setup(bot):
    bot.add_cog(Roles(bot))
