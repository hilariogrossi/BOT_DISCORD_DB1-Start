import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Robô logado como {self.user}!')

    async def on_message(self, message):
        print(f'Mensagem de {message.author}: {message.content}.')
        if message.content == '?regras':
            await message.channel.send(
                f'{message.author.name} as regras do servidor são:'
                f'{os.linesep}1- Desrespeito com qualquer membro da comunidade;'
                f'{os.linesep}2- Assédio moral ou sexual;'
                f'{os.linesep}3- Preconceito ou racismo;'
                f'{os.linesep}4- Envio de publicidade;'
                f'{os.linesep}5- Envio de conteúdo em massa;'
                f'{os.linesep}6- Promoção de conteúdos ou atividades ilegais (pirataria, violência, etc).')
        elif message.content == '?nivel':
            await message.author.send('Nível 1')
        elif message.content == '?nome':
            name = message.author
            await message.author.send(f'Olá {name}. Seja bem-vindo(a)!')

        if 'palavrão' in message.content:
            await message.channel.send(f'Por favor {message.author.name},'
                                       f' atende-se para às regras do canal.'
                                       f' Não se pode ofender os demais usuários.')
            await message.delete()

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            mensagem = f'{member.mention} acabou de entrar no {guild.name}'
            await guild.system_channel.send(mensagem)

