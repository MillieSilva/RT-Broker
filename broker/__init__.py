__all__ = ['database', 'app', 'api']

## System Imports

## Application Imports
from . import *

## Library Imports


def initialize_app(debug: bool):
	database.initialize()
	
	app.run(debug)

