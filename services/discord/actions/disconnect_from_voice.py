import services.discord.support.fetch as fetch
from services.discord.support.id_name_builder import id_name_builder
from services.discord.actions.base import Base

class DisconnectFromVoice(Base):
    @classmethod
    async def action(cls, guild_id):
        result = {}

        guild = await fetch.guild(guild_id, result)
        if not guild: return result

        voice_client = guild.voice_client

        if not voice_client:
            result['type'] = 'not_connected'
            return result
    
        await voice_client.disconnect()
        voice_client.cleanup()

        result['disconnected_channel'] =  id_name_builder(voice_client.channel)
        result['type'] = 'success'

        return result