## System Imports

## Application Imports
from broker import database
from broker.app import flask_app as application

## Library Imports


if __name__ == '__main__':
	database.initialize()
	application.run()

