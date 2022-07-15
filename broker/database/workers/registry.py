## System Imports
from uuid import UUID, uuid4

## Application Imports
from broker import database
from broker.database.workers import discovery

## Library Imports


def get_available_uuid() -> UUID:
	uuid = uuid4()
	
	while discovery.id_exists(uuid):
		uuid = uuid4()
	
	return uuid


def register(hwid: str) -> str | None:
	uuid = str(get_available_uuid())
	
	workers_cursor = database.database_connection.execute('''INSERT INTO Workers (Id, HwId) VALUES (?, ?)''',
														  (uuid, hwid))
	
	if not workers_cursor.rowcount == 1:
		return
	
	database.database_connection.commit()
	
	return uuid


def is_registered(hwid: str) -> bool:
	return get_uuid(hwid) is not None


def is_synchronized(uuid: str, ipv4: str) -> bool:
	cursor = database.database_connection.execute('''
			SELECT public_ipv4 FROM Addresses WHERE Id = ? AND public_ipv4 = ?;
		''', (uuid, ipv4))
	
	addressed = [row for row in cursor]
	
	if len(addressed) < 1:
		return False
	
	return True


def synchronize(uuid: str, ipv4: str):
	addresses_cursor = database.database_connection.execute('''
		INSERT INTO Addresses (Id, public_ipv4) VALUES (?, ?)
	''', (uuid, ipv4))
	
	if not addresses_cursor.rowcount == 1:
		return
	
	database.database_connection.commit()


def get_uuid(hwid: str) -> str | None:
	cursor = database.database_connection.execute('''
		SELECT Id FROM Workers WHERE Workers.HwId = ?;
	''', (hwid, ))
	
	uuids = [row for row in cursor]
	
	if len(uuids) < 1:
		return None
	
	return uuids[0][0]

