## System Imports

## Application Imports


## Library Imports
from flask import Flask
from flask_restx import Api

flask_app = Flask(__name__)
flask_api = Api(flask_app, version='1.0', title='RT Broker API', description='Remote Teller Broker Authentication API',)


def run(debug: bool):
	print()
	
	if debug:
		print("Running in Development mode")
	else:
		print("Running in Production mode")
	
	flask_app.run(debug=debug)

