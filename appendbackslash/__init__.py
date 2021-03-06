from redbot.core import commands


class AppendBackslash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="abs")
    async def _abs(self, ctx, text: str):
        """Add a backslash to the start of a string."""
        await ctx.send(f"\\{text}")


def setup(bot):
    bot.add_cog(AppendBackslash(bot))
