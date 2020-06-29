import numpy as np

def transformToGeoPoint(s):
    """
    Transforma lat and long en points para la geoquery
    """
    if np.isnan(s.latitude) or np.isnan(s.longitude):
        return None
    return {
        "type":"Point",
        "coordinates":[s.longitude, s.latitude]
    }
    
