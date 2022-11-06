import discord as discord_lib
import services.discord.client as client

discord = client.get()

async def specific_channel(channel_id, channel_type, result):
    channel = discord.get_channel(channel_id)
    result['channel'] = {
        'id': channel_id
    }

    if not type(channel) is channel_type:
        result['type'] = 'no_channel'
        return
    
    result['channel']['name'] = channel.name
    return channel

async def text_channel(channel_id, result={}):
    return await specific_channel(channel_id, discord_lib.channel.TextChannel, result)

async def voice_channel(channel_id, result={}):
    return await specific_channel(channel_id, discord_lib.channel.VoiceChannel, result)

async def guild(guild_id, result={}):
    guild = discord.get_guild(guild_id)

    if not guild:
        result['type'] = 'no_guild'
        result['guild'] = {
            'id': guild_id
        }
        return 

    result['guild'] = {
        'id': guild_id,
        'name': guild.name
    }

    return guild