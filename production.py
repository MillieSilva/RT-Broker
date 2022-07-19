## System Imports

## Application Imports
from broker import database
from broker.app import flask_app as application

## Library Imports


database.initialize()

if __name__ == '__main__':
	application.run()

