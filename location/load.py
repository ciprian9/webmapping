import requests
from django.contrib.gis.geos import Point
from .models import DublinBikes
from .dublin_bikes_api import json_data_import


# Data being inserted to the database
def run():
    json_data = json_data_import()
    for i in json_data:
        print(i)
        p = DublinBikes(available_bike_stands=i['available_bike_stands'], available_bikes=i['available_bikes'],
                        total_bike_stands=i['bike_stands'], stand_number=i['number'], stand_name=i['name'],
                        last_update=i['last_update'], position=i['positio'])

        p.save()
