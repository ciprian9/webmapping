from django.template.defaulttags import register
from location.distance_of_points import distance_checker

@register.filter
def getpos(dictionary, key):
    return dictionary[0].key


@register.filter
def find_distance(lat, lon, check_lat, check_lon):
    return distance_checker(lat, lon, check_lat, check_lon)


