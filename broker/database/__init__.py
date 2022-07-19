__all__ = ['workers']

## System Imports
from pathlib import Path
import sqlite3
from sqlite3 import Connection
from typing import Optional


## Application Imports
from . import *

## Library Imports


database_directory = f'data'
database_path = f'{database_directory}/metadata.sql'

database_connection: Optional[Connection] = None


def initialize():
	directory = Path(database_directory)
	path = Path(database_path)
	
	if not path.exists():
		if not directory.exists():
			directory.mkdir()
		
		connection = sqlite3.connect(database_path, check_same_thread=False)
		setup(connection)
	else:
		connection = sqlite3.connect(database_path, check_same_thread=False)
	
	global database_connection
	database_connection = connection
	

def setup(connection: Connection):
	workers.setup_tables(connection)

