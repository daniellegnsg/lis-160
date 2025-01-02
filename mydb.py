import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'trisdan2702',

	)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE adco")

print("All done!")