import asyncio
import discord as discord_lib
import services.discord.client as client

discord = client.get()

async def discord_function(message, channel_id):
    channel = discord.get_channel(channel_id)
    result = {}
    result['message'] = message
    result['channel'] = {
        'id': channel_id
    }

    if not type(channel) is discord_lib.channel.TextChannel:
        result['type'] = 'no_channel'
        return result
    await channel.send(message)

    result['type'] = 'success'
    result['channel']['name'] = channel.name

    return result

async def send_message_to_channel(message, channel_id):
    result = asyncio.run_coroutine_threadsafe(
        discord_function(message, channel_id),
        discord.loop
    )
    return result.result()
