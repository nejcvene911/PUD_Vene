import http.client

conn = http.client.HTTPSConnection("omgvamp-hearthstone-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "75791661f4mshe18cbffd10a10f0p19b179jsn7e232b78597a",
    'x-rapidapi-host': "omgvamp-hearthstone-v1.p.rapidapi.com"
    }

conn.request("GET", "/cards", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
