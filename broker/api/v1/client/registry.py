## System Imports
from uuid import uuid4

## Application Imports
from broker.app import flask_api

## Library Imports
from flask import request
from flask_restx import Resource


route = '/api/v1/client/discover'


@flask_api.route(f'{route}/update')
class ClientRegistryUpdate(Resource):
	
	def post(self):
		http_client_ip = request.remote_addr
		pass

