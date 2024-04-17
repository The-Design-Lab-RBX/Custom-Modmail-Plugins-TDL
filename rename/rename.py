import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

import datetime

class Rename(commands.Cog):
    """Rename a thread"""

    def __init__(self, bot):
        self.bot = bot

    @checks.thread_only()
    @checks.has_permissions(PermissionLevel.SUPPORTER)

    @commands.command()
    async def rename(self, ctx, *, request):
        try:
            await ctx.message.add_reaction('⏰')
            
            await ctx.channel.edit(name = request) # Edit channel name.
            
            await ctx.message.clear_reactions()
            await ctx.message.add_reaction('✅')
            
            embed = discord.Embed(
                title = 'Renamed',
                description = "Renamed the thread to " + request + ".",
                color = discord.Color.red()
            )

            await ctx.reply(embed = embed)

        except discord.errors.Forbidden:
            embed = discord.Embed(
                title = 'Forbidden',
                description = "Error - Bot can't perform this action due to permission levels.",
                color = discord.Color.red()
            )
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text = 'Rename')

            await ctx.reply(embed = embed)
            
            await ctx.message.clear_reactions()
            await ctx.message.add_reaction('❌')
        except:
            await ctx.message.clear_reactions()
            await ctx.message.add_reaction('❌')

async def setup(bot):
    await bot.add_cog(Rename(bot))