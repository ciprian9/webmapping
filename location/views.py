from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from .models import Location, WorldBorder
#from .serializer import LocationSerializer
import json, re
import requests
from django.core import serializers
from django.template.response import TemplateResponse
from .distance_of_points import distance_checker
from .dublin_bikes_api import json_data_import
from .models import DublinBikes


def json_all_stations(request):
    lat = request.GET['lat']
    long = request.GET['long']

    json_data = json_data_import()
    for i in json_data:
        DublinBikes.objects.all()
    all_data = DublinBikes.objects.all()
    results = {}
    # for every queryset in the list serialize it.
    data = serializers.serialize("json", all_data)
    results[0] = json.loads(data)
    regex = r'\(([^)]+)\)'

    for i in results[0]:
        coords = i['fields']['position']
        res = re.findall(regex, coords)
        blong, blat = res[0].split(' ')
        dist = distance_checker(lat, long, blat, blong)
        dist = float(dist) / 1000
        dist = round(dist, 2)
        i['distance'] = dist
    return JsonResponse(results)



def index(request):
    return TemplateResponse(request, 'location/index.html')

def all_stations(request):
#    json_data = json_data_import()
#    for i in json_data:
#        DublinBikes.objects.filter(stand_number=i['number']).update(available_bike_stands=i['available_bike_stands'], 
#                available_bikes=i['available_bikes'], last_update=i['last_update'])
#    all_data = DublinBikes.objects.all()
    return TemplateResponse(request, 'location/all_bike_stations.html')

def find_nearest_station(request):
 #   json_data = json_data_import()
 #   for i in json_data:
 #       DublinBikes.objects.filter(stand_number=i['number']).update(available_bike_stands=i['available_bike_stands'], 
 #              available_bikes=i['available_bikes'], last_update=i['last_update'])
 #   all_data = DublinBikes.objects.all()
    return TemplateResponse(request, 'location/find_nearest_station.html')


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

    all_data = DublinBikes.objects.all();
    reslts = {}
    data = serializers.serialize('json', all_data)
    results[0] = json.loads(data)
    regex = r'\(([^)]+)\)'

    for i in results[0]:
        coords = i['fields']['position']
        res = re.findall(regex, coords)
        blon, blat = res[0].split(' ')
        dist = distance_checker(lat, lng, blat, blong)
        dist = float(dist) / 1000
        dist = round(dist, 2)
        i['distance'] = dist
    results['lat'] = lat
    results['lng'] = lng
    return JsonResponse(results)






"""
@api_view(['GET', 'POST'])
def location_list(request, format=None):
    if request.method == 'GET':
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def location_detail(request, pk, format=None):
    try:
        location = Location.objects.get(pk=pk)
    except Location.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LocationSerializer(location)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def world_list(request, format=None):
    if request.method == 'GET':
        results = WorldBorder.objects.all()
        serializer = WorldBorderSerializer(results, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = WorldBorderSerializer(data=requst.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def world_detail(request, pk, format=None):
    try:
        world = WorldBorder.objects.get(pk=pk)
    except WorldBorder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WorldBorderSerializer(world)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WorldBorderSerializer(world, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        world.deleted()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""




