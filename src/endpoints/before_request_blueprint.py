import os
from flask import Blueprint
from flask import request
from src.views.view import load_view

before_request_blueprint = Blueprint(name="before_request_blueprint", import_name=__name__)

@before_request_blueprint.before_app_request
async def auth():
    integration_token = request.headers.get('authorization')
    if integration_token != os.getenv('INTEGRATION_TOKEN'):
        return load_view('authorization/failed')
