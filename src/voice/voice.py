from discord.ext import commands
from discord.ext.commands.core import command
from discord.ext.commands.errors import CommandInvokeError
import nacl

class VoiceChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def join(self, ctx):
        try: 
            channel = ctx.author.voice.channel
            await channel.connect()
        except:
            await ctx.send('Você não está em um canal de voz...')

    @commands.command() 
    async def leave(self, ctx):
        try:
            voice_client = ctx.message.guild.voice_client
            await voice_client.disconnect()
        except CommandInvokeError:
            pass