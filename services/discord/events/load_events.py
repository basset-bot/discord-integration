import services.discord.events.on_message as on_message

def load_events(discord):
    on_message.load(discord)