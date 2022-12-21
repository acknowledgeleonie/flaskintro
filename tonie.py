import mariadb
import json
import pandas as pd 

class Fiets:
    merk = 'nvt'


def methodevantonie():
	mydb = mariadb.connect(
    	host='localhost',
		username='root',
		password='',
		database='demo'
  )
 
	cursor = mydb.cursor()
	query = "SELECT * FROM fiets"
	cursor.execute(query)
	fietsen = cursor.fetchall()
	fiets1 = Fiets()
	fiets1.merk = fietsen[0][1]
	return json.dumps(fiets1.__dict__)

