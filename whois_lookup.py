import whois
import socket
import requests



def whois_lookup(url):
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

	w=whois.whois(url2)
	ed=w.expiration_date
	e=""
	try:
		e=ed.strftime("%a,%d %B,%Y")
	except:
		try:
			for each in ed:
				e=str(each)
				break
		except:
			e=str(ed)

	a={"Domain Expiry":e}
	return a


