from flask import Blueprint
from flask import request
from src.views.view import load_view
from services.discord.actions.disconnect_from_voice import DisconnectFromVoice
from services.discord.actions.play_music import PlayMusic

voice_channels_blueprint = Blueprint(name="voice_channels_blueprint", import_name=__name__)

@voice_channels_blueprint.route("/disconnect", methods = ['POST'])
async def disconnect_from_channel():
    guild_id = int(request.args.get('guild_id'))
    result = await DisconnectFromVoice.execute(guild_id)
    return load_view('voice_channels/disconnect/' + result['type'], result)

@voice_channels_blueprint.route("/play", methods = ['POST'])
async def play():
    guild_id = int(request.args.get('guild_id'))
    youtube_id = request.args.get('youtube_id')
    delay = request.args.get('delay')
    result = await PlayMusic.execute(guild_id, youtube_id, delay)
    return load_view('voice_channels/play/' + result['type'], result)