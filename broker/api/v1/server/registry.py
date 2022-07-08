## System Imports
from uuid import uuid4

## Application Imports
from flask_restx import Resource
from broker.app import flask_api

## Library Imports


route = '/api/v1/registry/server/'


@flask_api.route(f'{route}/update')
class ServerRegistryUpdate(Resource):
	pass
