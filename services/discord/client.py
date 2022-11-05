import os
import discord
import threading

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.none()
intents.reactions = True
intents.members = True
intents.guilds = True

client = discord.Client(intents=intents)

def get():
    return client

def run():
    client.run(TOKEN)