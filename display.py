import sqlite3 as sql


con=sql.connect("domain_data.db")
cur=con.cursor()
res=cur.execute("select * from domains")
html="<table><th>Serial</th><th>Domain</th><th>Expiry Date</th><th>Days Left</th>"
for each in res:
	html=html+"<tr>"
	for every in each:
		html=html+"<td>"+str(every)+"</td>"
		print(every)
	html=html+"/<tr>"
html=html+"</table>"

print(html)