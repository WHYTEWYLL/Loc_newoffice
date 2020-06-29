import pandas as pd
from pymongo import MongoClient
from src.geoQueryNear import *
def geoQueryNear(point,radius=10000):
    return {
        "geopoint":{
            "$near": {
                "$geometry": point,
                "$maxDistance": radius,
                "$minDistance": 0
            }
        }
    }
