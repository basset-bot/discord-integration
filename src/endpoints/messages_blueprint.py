from flask import Blueprint
from flask import request
from services.discord.send_message_to_channel import send_message_to_channel
from src.views.view import load_view

messages_blueprint = Blueprint(name="messages_blueprint", import_name=__name__)

@messages_blueprint.route("/send_to_channel", methods = ['POST'])
async def send_to_channel():
    channel_id = int(request.args.get('channel_id'))
    message = request.args.get('message')
    result = await send_message_to_channel(message, channel_id)
    return load_view('messages/send_to_channel/' + result['type'], result)
