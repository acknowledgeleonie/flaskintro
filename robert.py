import mariadb
import json

class Leprechaun:
	naam = 'David'
	bos = ''
	boom = ''

def methodevanrobert():
	#i_1 = "paddy"
	#i_2 = "lettuce"
	#i_3 = "tomatoe"
	#i_4 = "mushroom"
	#i_5 = "paddy"

	conn = mariadb.connect(
		host='localhost',
		username='root',
		password='',
		database='paddenstoelen'
	)

	cursor = conn.cursor()
	query="SELECT * FROM kabouters"
	cursor.execute(query)
	leprechauns = cursor.fetchall()
	
	leprechaun = Leprechaun()
	for element in leprechauns[1]:
		leprechaun.naam = leprechauns[1][1]#Zou Ferdinand moeten worden.
		leprechaun.bos = leprechauns[1][2]
		leprechaun.boom = leprechauns[1][3]
	return json.dumps(leprechaun.__dict__)
	#return ("Robert's special is {} + {} + {} + {} + {}".format(i_1,i_2,i_3,i_4,i_5))

methodevanrobert()