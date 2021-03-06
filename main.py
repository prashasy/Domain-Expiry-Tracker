import whois
import requests
import datetime
import sqlite3 as sql




def update(url,e,tte):
	conn=sql.connect("domain_data.db")
	cur=conn.cursor()
	cur.execute("""UPDATE domains
SET expiry = ?, tte = ? where domain=?""",(e,tte,url))
	print("data updated")
	conn.commit()
	conn.close()


def transact_db(url,e,tte):
	conn=sql.connect("domain_data.db")
	cur=conn.cursor()
	cur.execute("insert into domains(domain,expiry,tte)values(?,?,?)",(str(url),str(e),str(tte)))
	print("data inserted")
	conn.commit()
	conn.close()



def get_tte(d):
	try:
		tte=datetime.datetime.strptime(d,"%Y-%m-%d %H:%M:%S")-datetime.datetime.now()
	except:
		return -9999
	return tte.days

def get_data(url):
	url2=url
	p2=url[:3]
	if(url[:4]!="http" and p2!="www"):
		url="http://www."+url
	else:
		if(p2=="www"):
			url="http://"+url


	if(url[:5]=="https"):
		url2=url[8:]
	else:
		url2=url[7:]

	print("URl:"+url)
	print("URL2:"+url2)

	try:
		w=whois.whois(url2)
		ed=w.expiration_date
	except:
		return ["N/A","N/A"]

	e=""
	try:
		e=ed.strftime("%Y-%m-%d %H:%M:%S")
	except:
		try:
			for each in ed:
				e=str(each)
				break
		except:
			e=str(ed)

	ret=[]
	ret=[e,datetime.datetime.now()]

	return ret





def insert_url(url):
	conn=sql.connect("domain_data.db")
	cur=conn.cursor()
	res=get_data(url)
	e=res[0]
	tte=res[1]
	res=cur.execute("select 1 from domains where domain=?",(url,))
	op=res.fetchall()
	try:
		if(op[0][0]==1):
			print("entry exists...updating")
			update(url,e,tte)
	except:
		transact_db(url,e,tte)
	conn.commit()
	conn.close()





