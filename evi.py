import mariadb
import json

class persoonsgegevensq:
  voornaam = 'nvt'

def methodevanevi():
  mydb = mariadb.connect(
      host='localhost',
      username='root',
      password = '',
      database = 'personen'

    )

  cursor = mydb.cursor()
  query = "SELECT * FROM persoonsgegevens"
  cursor.execute(query) 
  persoonsgegevens = cursor.fetchall()
  persoon10 = persoonsgegevensq()
  persoon10.voornaam = persoonsgegevens[0][1]
  return json.dumps(persoon10.__dict__)

x = methodevanevi()
print (x)

def methodevanevi_1():
  return "Hallo, Evi hier."