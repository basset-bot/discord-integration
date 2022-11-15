from time import sleep
import asyncio
import services.discord.support.fetch as fetch
from services.discord.support.treated_youtube_stream import treated_youtube_stream
from services.discord.actions.base import Base

class PlayMusic(Base):
    @classmethod
    async def action(cls, guild_id, youtube_id, wait_voice_client_stop):
        result = {}
        result['youtube_id'] = youtube_id
        result['wait_voice_client_stop'] = wait_voice_client_stop
        
        guild = await fetch.guild(guild_id, result)
        if not guild: return result

        voice_client = guild.voice_client
        if not voice_client:
            result['type'] = 'not_connected'
            return result

        stream = await cls._fetch_stream(youtube_id, result)
        if not stream: return result


        playing = await cls.play(voice_client, stream) == 'playing'
        if not wait_voice_client_stop:
            if playing:
                result['type'] = 'already_playing'
            else:
                result['type'] = 'success'
                result['details'] = 'Playing succesfully'

            return result

        asyncio.run_coroutine_threadsafe(
            cls.play_loop(voice_client, stream, wait_voice_client_stop),
            cls.discord.loop
        )
        result['type'] = 'success'
        result['details'] = 'Succesfully enqueued'
        
        return result

    @classmethod
    async def _fetch_stream(cls, youtube_id, result):
        try:
            stream = treated_youtube_stream(youtube_id)
        except Exception as e:
            result['type'] = 'stream_error'
            result['stage'] = 'early'
            result['exception'] = repr(e)
            return

        if not stream:
            result['type'] = 'youtube_id_not_found'
            return

        return stream

    @classmethod
    async def play_loop(cls, voice_client, stream, wait_voice_client_stop):
        while await cls.play(voice_client, stream) == 'playing':
            if not wait_voice_client_stop:
                break
            sleep(1)

    @classmethod
    async def play(cls, voice_client, stream):
        try:
            await voice_client.play(stream)
        except TypeError:
            # not really sure why this is needed
            pass
        except Exception as e:
            if str(e) == 'Already playing audio.':    
                return 'playing'