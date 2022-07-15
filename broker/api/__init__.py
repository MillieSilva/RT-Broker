__all__ = ['v1']

## System Imports

## Application Imports
from . import v1
from broker.app import flask_api

## Library Imports
from flask import request, jsonify
from flask_restx import Resource
from flask_api import status


route = '/api/v1'


@flask_api.route(f'{route}/check_status')
class APICheckStatus(Resource):
	
	def get(self):
		result = jsonify({})
		result.status_code = status.HTTP_200_OK
		
		return result
