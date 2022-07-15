## System Imports

## Application Imports

## Library Imports


route = '/api/v1/watcher/registry'

"""
@flask_api.route(f'{route}/discover<string:uuid>')
class ClientWatcherRegistty(Resource):
	
	def get(self, uuid_string: uuid4):
		try:
			uuid = UUID(uuid_string)
		except ValueError:
			return 400
		
		return 400

"""

