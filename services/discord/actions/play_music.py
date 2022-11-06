from services.youtube.stream import get as get_stream
import services.discord.support.fetch as fetch
from services.discord.actions.base import Base

class PlayMusic(Base):
    @classmethod
    async def action(guild_id, youtube_id, delay):
        result = {}
        
        guild = fetch.guild(guild_id)
        if guild: return result

        voice_client = guild.voice_client

        if not voice_client:
            result['type'] = 'not_connected'
        else:
            stream = get_stream(youtube_id)

            result['type'] = 'success'
        
        return result