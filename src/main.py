import logging
from discord.ext import commands
from cogs.misc import Misc
from cogs.games import Games

# Criando meu logger: 
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler(filename='discord.log',
                              encoding='utf-8',
                              mode='w')

formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

bot = commands.Bot(command_prefix='.')

# Adicionando os comandos de outros arquivos:
bot.add_cog(Misc(bot))
bot.add_cog(Games(bot))

bot.run('kkkk')

