import threading
from flask import Flask
import services.discord.client as discord_client
from src.endpoints.messages_blueprint import messages_blueprint

app = Flask(__name__)
api_prefix = '/api/v1/'
app.register_blueprint(messages_blueprint, url_prefix=f"{api_prefix}messages/")

threading.Thread(target=discord_client.run).start()
