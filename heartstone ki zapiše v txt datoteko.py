import http.client
import time
from datetime import date

x=int(input("1-3:\n"))
if x==1:
    name="Vene.txt"
elif x==2:
    name="Nejc.txt"
else:
    name="Vene_"+str(date.today())+".txt"
    
file=open(name,"w")

conn = http.client.HTTPSConnection("omgvamp-hearthstone-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "75791661f4mshe18cbffd10a10f0p19b179jsn7e232b78597a",
    'x-rapidapi-host': "omgvamp-hearthstone-v1.p.rapidapi.com"
    }

conn.request("GET", "/cards?cost=25", headers=headers)

res = conn.getresponse()
data = res.read()

file.write(data.decode("utf-8"))

file.close()

file=open(name,"r")
print(file.read())
