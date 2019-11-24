import requests
import re

ObjRead = open("link.txt", "r")
 

link = ObjRead.read();

ObjRead.close()

data = requests.get(link)

phones = re.findall(r'(\(?[0-9]{3}\)?(?:\-|\s|\.)?[0-9]{3}(?:\-|\.)[0-9]{4})', data.text)
emails = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', data.text)

print("--------------------------------------")
print("Phone Numbers -", phones)
print("--------------------------------------")
print("Emails -", emails)
print("--------------------------------------")
print ("Data from -", link)
print("--------------------------------------")
input('Press ENTER to exit')
