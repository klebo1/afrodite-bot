from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith('afrodite'):
            await message.channel.send(f'Oi, {message.author.name}!')

    @commands.command()
    async def fala(self, ctx, *args):
        args = ' '.join(args)
        await ctx.send(args)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

    @commands.command()
    async def pong(self, ctx):
        await ctx.send('Ping!')