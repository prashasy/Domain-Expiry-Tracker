import sqlite3 as sql


def show():
	con=sql.connect("domain_data.db")
	cur=con.cursor()
	res=cur.execute("select * from domains ORDER BY tte ASC",())
	html="<table><th>Serial</th><th>Domain</th><th>Expiry Date</th><th>Days Left</th><th>Scan</th>"
	for each in res:
		html=html+"<tr>"
		for every in each:
			html=html+"<td>"+str(every)+"</td>"
			print(every)
		html=html+"<td><button id='run_subdomain_scan'>Scan Sub Domains</button></td></tr>"
	html=html+"</table>"
	print(html)
	return html
