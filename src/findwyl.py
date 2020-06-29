import os
from dotenv import load_dotenv
import requests,json

load_dotenv()

FOURSQUARE_CLIENTID= os.getenv("nombrefour")
FOURSQUARE_CLIENTSECRET= os.getenv("clavefour")

def findwyl(center,thing):
    url = 'https://api.foursquare.com/v2/venues/explore'
    params = dict(
    client_id=FOURSQUARE_CLIENTID,
    client_secret=FOURSQUARE_CLIENTSECRET,
    v='20200628',
    ll=f"{center[0]},{center[1]}",
    query=f"{thing}",
    radius=10000,limit=10)
    res=requests.get(url,params=params)
    respuesta=res.json()
    print(respuesta)
    sitios=[]
    for i in range(len(respuesta["response"]["groups"][0]['items'])):
        a={
        "Place":thing,
        "address":" ".join(respuesta["response"]["groups"][0]['items'][i]['venue']["location"]['formattedAddress']),
        "distance": (respuesta["response"]["groups"][0]['items'][i]['venue']["location"]['distance'])/1000,
        "location":respuesta["response"]["groups"][0]['items'][i]['venue']["location"],
        "latitude":respuesta["response"]["groups"][0]['items'][i]['venue']["location"]['lat'],
        "longitude":respuesta["response"]["groups"][0]['items'][i]['venue']["location"]['lng']
              
        }
        sitios.append(a)
    return sitios