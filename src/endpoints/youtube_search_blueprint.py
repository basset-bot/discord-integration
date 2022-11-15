from flask import Blueprint
from flask import request
from src.views.view import load_view
from services.discord.actions.disconnect_from_voice import DisconnectFromVoice

youtube_search_blueprint = Blueprint(name="youtube_search_blueprint", import_name=__name__)

@youtube_search_blueprint.route("/youtube_search", methods = ['GET'])
async def search_video():
    guild_id = int(request.args.get('guild_id'))
    result = await DisconnectFromVoice.execute(guild_id)
    return load_view('video/' + result['type'], result)