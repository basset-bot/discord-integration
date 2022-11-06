import asyncio
import discord as discord_lib
import services.discord.client as client

discord = client.get()

async def discord_function(channel_id):
    result = {}
    result['channel'] = {
        'id': channel_id,
    }

    channel = discord.get_channel(channel_id)

    if not type(channel) is discord_lib.channel.VoiceChannel:
        result['type'] = 'no_channel'
        return result

    result['channel']['name'] = channel.name
    voice_client = channel.guild.voice_client

    if voice_client:
        result['type'] = 'already_connected'
        result['connected_channel'] = {
            'id': voice_client.channel.id,
            'name': voice_client.channel.name
        } 
        return result    

    asyncio.run_coroutine_threadsafe(
        channel.connect(),
        discord.loop
    )

    result['type'] = 'success'
    return result

async def connect_to_voice(channel_id):
    result = asyncio.run_coroutine_threadsafe(
        discord_function(channel_id),
        discord.loop
    )
    
    return result.result()