## System Imports
from sqlite3 import Connection

## Application Imports

## Library Imports


def setup_tables(connection: Connection):
	connection.execute('''
		CREATE TABLE Workers (
			 Id 			CHAR(38)     	NOT NULL,
			 HwId			CHAR(40)		NOT NULL,
			 PRIMARY KEY (Id, HwId),
			 UNIQUE (Id, HwId)
		);
	''')
	
	connection.execute('''
		CREATE TABLE Addresses (
			 Id 			CHAR(38) 		PRIMARY KEY     	NOT NULL,
	         public_ipv4    CHAR(15)     						NOT NULL
		);
	''')

