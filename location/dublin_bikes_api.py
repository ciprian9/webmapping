import datetime
import requests
from django.contrib.gis.geos import Point
from django.utils import timezone

"""
    function to retrieve data from the dublin bikes api to load
    it in the database
"""
def json_data_import():
    #create a request to receive the data from the api
    r = requests.get(
             'https://api.jcdecaux.com/vls/v1/stations?contract=Santander&apiKey=a6c1b6c4bac2222a2b80e49abf91bbfddd45e5e2')
    #translate the data to json format
    dub_json_data = r.json()
    #loop around the json data 
    for i in dub_json_data:
        #update the last_update field
        i['last_update'] = datetime.datetime.now()
        #update the position of the lat and lon
        i['positio'] = Point(float(i['position']['lng']), float(i['position']['lat']))
    #return the json data
    return dub_json_data

