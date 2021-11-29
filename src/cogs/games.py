import random
from discord.ext import commands
import asyncio
from time import sleep

char_invalidos = ('.', '!', '@', '$', 
                  '#', '%', '&', '*', 
                  '(', ')', '?', '/',
                  '<', '>', '[', ']',
                  '+', '=', '-', '\'',
                  '\"', ':', ';', '`',
                  ',', '_', '-', '^',
                  '{', '}',)

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Guess the number:
    @commands.command()
    async def advinhar(self, ctx):
        await ctx.send('Pensei em um número de 0 a 10, tente advinhar qual é!')
        escolha_afrodite = random.randint(0, 10)
        try:
            escolha_jogador = await self.bot.wait_for('message', timeout=10.0)
        except asyncio.TimeoutError:
            await ctx.send('Demorou demais...')
        
        valido = escolha_jogador.content.isnumeric()
        if valido:
            if int(escolha_jogador.content) == escolha_afrodite: 
                await ctx.send(f'Acertou! Eu pensei no número {escolha_afrodite}!!')
            else: 
                await ctx.send(f'Não foi dessa vez... eu pensei no número {escolha_afrodite}!')
        else:
            await ctx.send('Escolha inválida...')

    # Jogo da forca:
    @commands.command()
    async def forca(self, ctx):
        await ctx.send('Bem-vindo ao Jogo da Forca!')
        arquivos = ['frutas.txt', 'objetos.txt']
        escolhido = arquivos[random.randrange(0, len(arquivos))]
        arquivo = open(f'forca/{escolhido}', 'r')
        palavras_possiveis = []
        letras_certas = []

        for linha in arquivo:
            palavras_possiveis.append(linha)

        arquivo.close
        palavra_secreta = palavras_possiveis[random.randrange(len(palavras_possiveis))]
        palavra_secreta = palavra_secreta.upper()

        for letra in range(1, len(palavra_secreta)):
            letras_certas.append('_')

        escolhido = escolhido.replace('s.txt', '')

        sleep(3)

        await ctx.send('A dica é: {}\n``{}``'.format(escolhido, ' '.join(letras_certas)))

        acertou = False
        perdeu = False
        tentativas = 5 
        
        while not acertou and not perdeu:
            try:
                # Recebendo o input de uma mensagem:
                chute = await self.bot.wait_for('message', timeout=60)
                str_chute = chute.content.upper()
                # Criando uma variavel pra armazenar o chute
                if len(str_chute) == 1:
                    if str_chute not in char_invalidos:
                        if str_chute in palavra_secreta:
                            posicao = 0
                            for letra in palavra_secreta:
                                if str_chute == letra:
                                    letras_certas[posicao] = str_chute

                                posicao += 1
                        # Acima checando se ela está na palavra.
                        else:
                            tentativas -= 1
                            await ctx.send(f'A letra {str_chute} não está na palavra! Restam {tentativas} tentativas...')

                        await ctx.send('``{}``'.format(' '.join(letras_certas)))


                perdeu = tentativas == 0
                acertou = '_' not in letras_certas

                if perdeu: await ctx.send(f'Que pena, você perdeu...\nA palavra certa era {palavra_secreta.lower()}')

                if acertou: await ctx.send(f'Parabéns! A palavra certa era {palavra_secreta.lower()}')


            except asyncio.TimeoutError:
                await ctx.send('Que pena, você perdeu a vez.....')
                perdeu = True

