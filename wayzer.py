import requests
import time
print("Input wayzer mapid\n")
id = input()
url = "https://mdt.wayzer.top/api/maps/"+id+"/download.msav"
res = requests.get(url)

with open('map-'+str(int(time.time()))+".msav", 'wb') as f:
    f.write(res.content)

url2 = "https://mdt.wayzer.top/api/maps/"+id+"/detail.json"
res2 = requests.get(url2)

with open('detail-'+str(int(time.time()))+".json", 'wb') as f:
    f.write(res2.content)