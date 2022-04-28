from collections import UserList
import discord
from discord.ext import commands
from discord import Attachment
import aiosqlite

db_path = "./database.db"




class modsetup(commands.Cog):
    """Moderation setup commands such as wordfilters"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="setup")
    async def setup(self, ctx, option = None, channel : discord.TextChannel = None, userchannel : discord.TextChannel = None):
        """sets up certain moderation actions use setup command without args to see all options.\nwordfilter format: wordfilter + attach an txt file with each bad word on a new line.\nLogs format: logs #channelForMessageLogs #ChannelForUserLog"""
        if option == "wordfilter":
            if ctx.message.attachments is None:
                return await ctx.send("Make sure to attach a file!")
            else:
                try:
                    await ctx.message.attachments[0].save(fp=f"./wordfilters/{ctx.guild.id}.txt")
                except IndexError:
                    return await ctx.send("Please add a txt file with each bad word on a new line with your message.")
                return await ctx.send(f"saved the wordfilter as {ctx.guild.id}.txt and was uploaded by {ctx.author.display_name} ")
        elif option == "logs":
            if channel == None:
                return await ctx.send("Please mention a channel for message logs.")
            elif userchannel == None:
                return await ctx.send("Please mention a channel for user logs.")
            db = await aiosqlite.connect(db_path)
            await db.execute("INSERT OR IGNORE INTO logchannels VALUES (?, ?, ?)", (ctx.guild.id, channel.id, userchannel.id,))
            await db.commit()
            try:
                await db.close()
            except ValueError:
                pass
            return await ctx.send(f"✅ Set Message channel to {channel.name} and user log channel to {userchannel.name}.")
        elif option == None:
            return await ctx.send("All available options: **wordfilter, logs**")

            

    



def setup(bot):
    bot.add_cog(modsetup(bot))