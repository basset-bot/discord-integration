import threading
from flask import Flask
from dotenv import load_dotenv
import services.discord.client as discord_client
from src.endpoints.messages_blueprint import messages_blueprint
from src.endpoints.before_request_blueprint import before_request_blueprint

load_dotenv()

app = Flask(__name__)
api_prefix = '/api/v1/'
app.register_blueprint(before_request_blueprint)
app.register_blueprint(messages_blueprint, url_prefix=f"{api_prefix}messages/")

threading.Thread(target=discord_client.run).start()
