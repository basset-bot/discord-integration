from discord import FFmpegPCMAudio
from services.youtube.get_stream import get_stream

FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'
    }

def treated_youtube_stream(youtube_id):
    stream = get_stream(youtube_id)
    if not stream: return
    source = FFmpegPCMAudio(stream.url, **FFMPEG_OPTIONS)
    return source
    