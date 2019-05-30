import whois
import socket
import requests



def whois_lookup(url):
	w=whois.whois(url)
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


