import discord
from discord import app_commands
from discord.ext import commands

class Graphs(commands.cog):
    def __init__(self, bot):
        self.bot = bot


async def setup(bot):
    await bot.add_cog(Graphs(bot))