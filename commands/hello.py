from discord.ext import commands


class Greeting(commands.Cog):
    @commands.command()
    async def hello(self, ctx):
        await ctx.send('Hello {0.display_name'.format(ctx.author))


def setup(bot):
    bot.add_cog(Greeting(bot))
