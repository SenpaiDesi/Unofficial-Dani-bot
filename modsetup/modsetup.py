import discord
from discord.ext import commands
from discord import Attachment





class modsetup(commands.Cog):
    def __init__(self, bot):
        """Moderation setup commands such as wordfilters"""
        self.bot = bot

    @commands.command(name="wordfilter")
    async def save(self, ctx):
        """Saves a list of words to filter. Ussage: wordfilter <Attach an txt file with each word on a new line to this message>"""
        if ctx.message.attachments is None:
            return await ctx.send("Make sure to attach a file!")
        else:
            await ctx.message.attachments[0].save(fp=f"./wordfilters/{ctx.guild.id}.txt")

            return await ctx.send(f"saved the wordfilter as {ctx.guild.id}.txt and was uploaded by {ctx.author.display_name} ")

    



def setup(bot):
    bot.add_cog(modsetup(bot))