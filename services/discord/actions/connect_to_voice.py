import asyncio
import services.discord.support.fetch as fetch
from services.discord.support.id_name_builder import id_name_builder
from services.discord.actions.base import Base

class ConnectToVoice(Base):
    @classmethod
    async def action(cls, channel_id):
        result = {}

        channel = await fetch.voice_channel(channel_id, result)
        if not channel: return result

        voice_client = channel.guild.voice_client
        
        if voice_client:
            result['type'] = 'already_connected'
            result['connected_channel'] = id_name_builder(voice_client.channel)
            return result    

        asyncio.run_coroutine_threadsafe(
            channel.connect(),
            cls.discord.loop
        )

        result['type'] = 'success'
        return result