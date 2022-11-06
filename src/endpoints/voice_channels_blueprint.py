from flask import Blueprint
from flask import request
from src.views.view import load_view
from services.discord.connect_to_voice import connect_to_voice
from services.discord.disconnect_from_voice import disconnect_from_voice

voice_channels_blueprint = Blueprint(name="voice_channels_blueprint", import_name=__name__)

@voice_channels_blueprint.route("/connect", methods = ['POST'])
async def connect_to_channel():
    channel_id = int(request.args.get('channel_id'))
    result = await connect_to_voice(channel_id)
    return load_view('voice_channels/connect/' + result['type'], result)

@voice_channels_blueprint.route("/disconnect", methods = ['POST'])
async def disconnect_from_channel():
    guild_id = int(request.args.get('guild_id'))
    result = await disconnect_from_voice(guild_id)
    return load_view('voice_channels/disconnect/' + result['type'], result)