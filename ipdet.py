import urllib.request
import json,webbrowser,pprint
f=open("ip.txt","r")
ipd=f.readline()
ipadd=ipd[3:]
ipaddre=ipadd.strip()
fuckip=urllib.request.urlopen("http://www.ip-api.com/json/"+ipaddre+"?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query").read()
parsed = json.loads(fuckip)
print(json.dumps(parsed, indent=4, sort_keys=True))
print("\n")
print("Coded by")
print("HARSH VARDHAN GOSWAMI")
print("\n")
