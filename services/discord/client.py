import os
import discord
from services.discord.events.load_events import load_events

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.reactions = True
intents.members = True
intents.guilds = True
intents.message_content = True

client = discord.Client(intents=intents)
load_events(client)

def get():
    return client

def run():
    client.run(TOKEN)