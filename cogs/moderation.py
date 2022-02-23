import disnake
from disnake.ext import commands
from disnake import member

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def my_kick_command(self, ctx, member: disnake.Member):
        await member.kick()
        await ctx.send(f"**{member.name}** has been kicked by **{ctx.author.name}**!")

def setup(bot):
    bot.add_cog(Moderation(bot)) # Add the class to the cog.