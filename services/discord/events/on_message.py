import os
from services.discord.support.connect_to_author_voice import connect_to_author_voice

PREFIX = os.getenv('PREFIX')
VOICE_CONNECT_COMMANDS = os.getenv('VOICE_CONNECT_COMMANDS').split(',')

def load(discord):
    @discord.event
    async def on_message(message):
        if not message.content.startswith(PREFIX):
            return
        
        no_prefix_message = message.content[len(PREFIX):]
        command, *_ = no_prefix_message.split(' ')

        if command in VOICE_CONNECT_COMMANDS:
            await connect_to_author_voice(message)

