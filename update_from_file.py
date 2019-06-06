import main
import display



f=open("domains.txt",'r')
for each in f:
	url=each.strip()
	main.insert_url(url)

print("done")