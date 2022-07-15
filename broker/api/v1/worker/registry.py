## System Imports
from uuid import UUID
from ipaddress import IPv4Address

## Application Imports
from broker.app import flask_api
from broker.database.workers import registry

## Library Imports
from flask import request, jsonify
from flask_restx import Resource
from flask_api import status


route = '/api/v1/worker/registry'

"""
@flask_api.route(f'{route}/register')
class ClientRegistryRegister(Resource):
	
	def post(self):
		http_client_ipv4 = request.remote_addr
		uuid = registry.register(IPv4Address(http_client_ipv4))
		
		if not uuid:
			response = jsonify({'content': 'Could not register due to internal issue'})
			response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
		
		response = jsonify({'uuid': uuid})
		response.status_code = status.HTTP_200_OK
		
		return response
"""


@flask_api.route(f'{route}/synchronize<string:hwid>')
class ClientRegistrySynchronize(Resource):
	
	def post(self, hwid: str):
		ipv4 = request.remote_addr
		
		if len(hwid) != 40:
			response = jsonify({'error': 'Provided HWID is not valid'})
			response.status_code = status.HTTP_400_BAD_REQUEST
			
			return response
		
		uuid = None
		if not registry.is_registered(hwid):
			uuid = registry.register(hwid)
		else:
			uuid = registry.get_uuid(hwid)
		
		if not uuid:
			response = jsonify({'error': 'Cannot register/synchronize due to unknown reason'})
			response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
			
			return response
		
		if not registry.is_synchronized(uuid, ipv4):
			registry.synchronize(uuid, ipv4)
		
		response = jsonify({'uuid': uuid})
		response.status_code = status.HTTP_200_OK
		
		return response

