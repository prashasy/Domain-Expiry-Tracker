import sqlite3 as sql


con=sql.connect("domain_data.db")
cur=con.cursor()
res=cur.execute("select * from domains")
for each in res:
	print(each)