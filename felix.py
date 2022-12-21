import mariadb
import json
import os

class Fiets:
    merk = 'nvt'

def methodevanfelix():
    if os.getenv('XAMPP_AAN'):
        mydb = mariadb.connect(
            host='localhost',
            username='root',
            password='',
            database='havendb'
        )
        cursor = mydb.cursor()

        query = "SELECT * FROM fiets"
        cursor.execute(query)
        fietsen = cursor.fetchall()
        fiets1 = Fiets()
        fiets1.merk = fietsen[0][1]
        return json.dumps(fiets1.__dict__)
    return "Flask app niet gedraaid met Xampp modus"

x = methodevanfelix()
print(x)