#from django.shortcuts import render

# Create your views here.
#from rest_framework import status
#from rest_framework.decorators import api_view
#from rest_framework.response import Response
#from .models import Location, WorldBorder
#from .serializer import LocationSerializer
import json, re
import requests
from django.http import JsonResponse
from django.core import serializers
from django.template.response import TemplateResponse
from .distance_of_points import distance_checker
from .dublin_bikes_api import json_data_import
from .models import DublinBikes
from .sql_selector import SELECT_ALL_DATA_VALUES


#json data view returns all the data in json format
def json_all_stations(request):
    #retrieve the users latituded and longitude
    lat = request.GET['lat']
    long = request.GET['long']
    
    #make a call to json data import to retrieve the json data from the api
    json_data = json_data_import()
    for i in json_data:
        DublinBikes.objects.all()
    all_data = SELECT_ALL_DATA_VALUES
    results = {}
    # for every queryset in the list serialize it.
    data = serializers.serialize("json", all_data)
    results[0] = json.loads(data)
    regex = r'\(([^)]+)\)'
    
    #set the format of the data to return it  
    for i in results[0]:
        coords = i['fields']['position']
        res = re.findall(regex, coords)
        blong, blat = res[0].split(' ')
        #calculate the distance
        dist = distance_checker(lat, long, blat, blong)
        dist = float(dist) / 1000
        dist = round(dist, 2)
        #save the distance
        i['distance'] = dist
    return JsonResponse(results)


#use index template for the index page
def index(request):
    return TemplateResponse(request, 'location/index.html')

def json_nearest_station(request):
        # Request address from form input
    address = request.GET.get('address')
    address = address + " dublin ireland"
    google_url = "https://maps.googleapis.com/maps/api/geocode/json?mode=walking&address={0}".format(address)
    # Google api requires underscores so replaces space default + symbol
    google_url = google_url.replace("+", "_")
    google_reply = requests.get(google_url)
    # Get the google reply request (string format) Make it into JSON
    location_data = json.loads(google_reply.text)
    # Parse lat and lng data
    lat = location_data['results'][0]['geometry']['location']['lat']
    lng = location_data['results'][0]['geometry']['location']['lng']

    json_data = json_data_import()
    for i in json_data:
        DublinBikes.objects.all()

    all_data = SELECT_ALL_DATA_VALUES
    reslts = {}
    data = serializers.serialize('json', all_data)
    results[0] = json.loads(data)
    regex = r'\(([^)]+)\)'

    for i in results[0]:
        coords = i['fields']['position']
        res = re.findall(regex, coords)
        blong, blat = res[0].split(' ')
        dist = distance_checker(lat, lng, blat, blong)
        dist = float(dist) / 1000
        dist = round(dist, 2)
        i['distance'] = dist
    results['lat'] = lat
    results['lng'] = lng
    return JsonResponse(results)


