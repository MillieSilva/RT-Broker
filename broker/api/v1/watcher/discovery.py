## System Imports

## Application Imports
from broker.app import flask_api
from broker.database.workers import discovery

## Library Imports
from flask_restx import Resource
from flask_api import status
from flask import jsonify


route = '/api/v1/watcher/discovery'


@flask_api.route(f'{route}/discover_all')
class ClientWatcherDiscoveryAll(Resource):
	
	def get(self):
		clients = discovery.get_all_ids()
		
		result = jsonify({'ids': clients})
		result.status_code = status.HTTP_200_OK
		
		return result


@flask_api.route(f'{route}/discover<string:uuid>')
class ClientWatcherDiscoveryDiscover(Resource):
	
	def get(self, uuid: str):
		uuid_object = str(uuid)
		
		client = discovery.get_metadata(uuid)
		
		response = jsonify(client)
		response.status_code = status.HTTP_200_OK
		
		return response

