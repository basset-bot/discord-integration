async def connect_to_author_voice(message):
    if message.guild.voice_client: return
    channel = message.author.voice.channel
    await channel.connect()