## System Imports
from uuid import uuid4

## Application Imports
from broker.app import flask_api

## Library Imports
from flask_restx import Resource


route = '/api/v1/client/discovery'


@flask_api.route(f'{route}/discover<string:uuid>')
class ClientDiscovery(Resource):
	
	def get(self, uuid: uuid4):
		return 400

