from typing_extensions import Self
import disnake
from disnake.ext import commands
from disnake import AllowedMentions, member, channel, role, guild

class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    #UNDER DEVELOPMENT