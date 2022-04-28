import discord
from discord.ext import commands



class messagelog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            f = open(f"./wordfilters/{message.guild.id}.txt")
            words = f.read().split()
            for word in words:
                if word in message.content:
                    await message.delete()
                    f.close()
                else:
                    pass
        except FileNotFoundError:
            pass



def setup(bot):
    bot.add_cog(messagelog(bot))