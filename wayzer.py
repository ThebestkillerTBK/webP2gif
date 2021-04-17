import requests
import json
print("Input wayzer mapid(example:10541)\n")
id = input()
url = 'https://mdt.wayzer.top/api/maps/thread/'+id+'/latest'
res = requests.get(url)


d = json.loads(res.text)
maphash = d['hash'].replace('-','')
mapname = d['tags']['name']
with open('detail-'+mapname+".json", 'wb') as f:
    f.write(res.content)

url2 = "https://mdt.wayzer.top/api/maps/"+maphash+"/download.msav"
res2 = requests.get(url2)

with open('map-'+mapname+".masv", 'wb') as f:
    f.write(res2.content)

