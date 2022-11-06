import asyncio
import services.discord.client as client

discord = client.get()

async def discord_function(guild_id):
    result = {}
    guild = discord.get_guild(guild_id)

    if not guild:
        result['type'] = 'no_guild'
        result['guild'] = {
            'id': guild_id
        }
        return result 

    result['guild'] = {
        'id': guild_id,
        'name': guild.name
    }

    voice_client = guild.voice_client

    if not voice_client:
        result['type'] = 'not_connected'
    else:
        # this is a famous GAMBIARRA
        # disconnects bot
        member = guild.get_member(discord.user.id) 
        await member.move_to(None)

        result['disconnected_channel'] =  {
            'id' : voice_client.channel.id,
            'name' : voice_client.channel.name
        }
        result['type'] = 'success'
    

    return result

async def disconnect_from_voice(channel_id):
    result = asyncio.run_coroutine_threadsafe(
        discord_function(channel_id),
        discord.loop
    )
    
    return result.result()