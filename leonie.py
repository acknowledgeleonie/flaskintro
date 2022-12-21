import mariadb
import json

def methodevanleonie():

    class Fiets:
        merk = "nvt"

    mydb = mariadb.connect(
        host =
        username =
        password =
        database=
    )

    cursor = mydb.cursor()
    query = "SELECT * FROM fietsen"
    cursor.execute(query)
    fietsen = cursor.fetchall()
    #print(fietsen)

    fiets1 = Fiets()
    fiets1.merk = fietsen[0][1]
    print(fietsen)

    return json.dumps(fiets1.__dict__)


x = methodevanleonie()
print(x)