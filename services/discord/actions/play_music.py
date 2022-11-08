import services.discord.support.fetch as fetch
from services.discord.support.treated_youtube_stream import treated_youtube_stream
from services.discord.actions.base import Base

class PlayMusic(Base):
    @classmethod
    async def action(cls, guild_id, youtube_id, delay):
        result = {}
        result['youtube_id'] = youtube_id
        result['delay'] = delay
        
        guild = await fetch.guild(guild_id, result)
        if not guild: return result

        voice_client = guild.voice_client

        if not voice_client:
            result['type'] = 'not_connected'
            return result

        try:
            stream = treated_youtube_stream(youtube_id)
        except Exception as e:
            result['type'] = 'stream_error'
            result['stage'] = 'early'
            result['exception'] = repr(e)
            return result

        if not stream:
            result['type'] = 'youtube_id_not_found'
            return result
        
        try:
            await voice_client.play(stream)
        except TypeError:
            # not really sure why this is needed
            pass
        except Exception as e:
            result['type'] = 'stream_error'
            result['stage'] = 'late'
            result['exception'] = repr(e)
            return result

        result['type'] = 'success'
        
        return result