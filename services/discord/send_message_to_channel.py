import asyncio
import services.discord.client as client

discord = client.get()

async def discord_function(message, channel_id):
    channel = discord.get_channel(channel_id)
    await channel.send(message)

async def send_message_to_channel(message, channel_id):
    asyncio.run_coroutine_threadsafe(
        discord_function(message, channel_id),
        discord.loop
    )