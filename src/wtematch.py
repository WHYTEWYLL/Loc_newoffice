import pandas as pd
from pymongo import MongoClient
from src.geoQueryNear import *
def wtematch(datany):
    resultados=[]
    for street in datany["geopoint"]:
        try:
            q=db.offices.find(geoQueryNear(street, radius=500),{"_id":0,"company_id":0})
            resultados+=q
        except Exception as e:
            continue
    return resultados