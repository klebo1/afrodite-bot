import random
from discord.ext import commands
import asyncio

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def advinhar(self, ctx):
        await ctx.send('Pensei em um número de 0 a 10, tente advinhar qual é!')
        escolha_afrodite = random.randint(0, 10)
        try:
            escolha_jogador = await self.bot.wait_for('message', timeout=10.0)
        except asyncio.TimeoutError:
            await ctx.send('Demorou demais...')
        if int(escolha_jogador.content) == escolha_afrodite: 
            await ctx.send(f'Acertou! Eu pensei no número {escolha_afrodite}!!')
        else: 
            await ctx.send(f'Não foi dessa vez... eu pensei no número {escolha_afrodite}!')

