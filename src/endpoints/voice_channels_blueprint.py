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

def treat_wait_voice_client_stop(wait_voice_client_stop):
    if wait_voice_client_stop in ['0', '1']:
        return int(wait_voice_client_stop)
    else:
        return 0

@voice_channels_blueprint.route("/play", methods = ['POST'])
async def play():
    guild_id = int(request.args.get('guild_id'))
    youtube_id = request.args.get('youtube_id')
    wait_voice_client_stop = request.args.get('wait_voice_client_stop')
    wait_voice_client_stop = treat_wait_voice_client_stop(wait_voice_client_stop) 
    
    result = await PlayMusic.execute(guild_id, youtube_id, wait_voice_client_stop)
    return load_view('voice_channels/play/' + result['type'], result)