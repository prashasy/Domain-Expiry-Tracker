import sqlite3 as sql


def create():
	con=sql.connect("domain_data.db")
	
	print("Database created successfully")
	cur=con.cursor()
	cur.execute("create table domains (id integer primary key auto increment,expiry text,tte int)")
	print("Table domains created successfully!!")

	con.commit()
	con.close()

sql_connect()