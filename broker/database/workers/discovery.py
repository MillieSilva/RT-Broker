## System Imports
from uuid import UUID
from sqlite3 import Cursor

## Application Imports
from broker import database

## Library Imports


def get_id(uuid: UUID) -> Cursor:
	uuid_str = str(uuid)
	cursor = database.database_connection.execute('''SELECT ID FROM Workers WHERE ID = (?)''',
												  (uuid_str, ))
	
	return cursor


def id_exists(uuid: UUID) -> bool:
	return get_id(uuid).rowcount > 0


def get_all_ids():
	cursor = database.database_connection.execute('''SELECT ID FROM Workers''')
	
	return [row[0] for row in cursor]


def get_metadata(uuid: UUID):
	uuid_str = str(uuid)
	
	cursor = database.database_connection.execute('''
		SELECT Addresses.public_ipv4 FROM Workers JOIN Addresses
	    ON Addresses.Id = Workers.Id WHERE Workers.Id = ?;
	''', (uuid_str, ))
	
	information = {
		'uuid': uuid,
		'public_ipv4': [row[0] for row in cursor]
	}
	
	return information

