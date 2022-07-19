__all__ = ['database', 'app', 'api']

## System Imports

## Application Imports
from . import *

## Library Imports


def initialize_app():
	database.initialize()
	app.flask_app.run()

