## System Imports
from pathlib import Path
import sqlite3

## Application Imports

## Library Imports

database_directory = f'data'
database_path = f'{database_directory}/metadata.sql'


def setup():
	directory = Path(database_directory)
	
	if not directory.exists():
		directory.mkdir()
	
	sqlite3.connect(database_path)
	
