from flask import Blueprint
from flask import request
from services.discord.send_message_to_channel import send_message_to_channel

messages_blueprint = Blueprint(name="messages_blueprint", import_name=__name__)

@messages_blueprint.route("/send_to_channel", methods = ['POST'])
async def send_to_channel():
    channel_id = int(request.args.get('channel_id'))
    message = request.args.get('message')
    await send_message_to_channel(message, channel_id)
    return {'message':message}, 200
