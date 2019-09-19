import sqlite3 as sql


def create():
	con=sql.connect("domain_data.db")
	
	print("Database created successfully")
	cur=con.cursor()
	cur.execute("create table domains(id integer primary key autoincrement,domain text,expiry text,last updated text,tte text)")
	print("Table domains created successfully!!")

	con.commit()
	con.close()

