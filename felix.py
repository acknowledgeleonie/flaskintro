import os
if os.getenv('XAMPP_AAN'):
    import mariadb
    import json

    class Fiets:
        merk = 'nvt'

    def methodevanfelix():
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

    x = methodevanfelix()
    print(x)
else:
    def methodevanfelix():
        return "De server is gestart zonder Xampp modus"