import discord
from Programa import programa
from Token import token

intents = discord.Intents.default()
intents.members = True

client = programa.MyClient(intents=intents)

client.run(token.TOKEN)
