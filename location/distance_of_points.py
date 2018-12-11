import pyproj as proj
from shapely import geometry
"""
function to return the distance between two points used to provide distance for directions 
parameters - lat and lon for point one 
             check_lat, check_lon for point two
             shapely used for point manipulation
"""
def distance_checker(lat, lon, check_lat, check_lon, shapely=None):
    #ESPG:4326(WGS84) - Initiate coords system for GeoJSON
    crs_wgs = proj.Proj(init='epsg:4326')
    #ESPG:27700(OSGB 1936) Initialise British National Grid as it covers Ireland aswell
    crs_bng = proj.Proj(init='epsg:27700')
    #convert the points to XY coordinates 
    x1, y1 = proj.transform(crs_wgs, crs_bng, lon, lat)
    #covert second point to XY coords
    x2, y2 = proj.transform(crs_wgs, crs_bng, check_lon, check_lat)
    #create point one and two using x1 y1 and x2 y2
    point_1 = geometry.Point(x1, y1)
    point_2 = geometry.Point(x2, y2)
    #return the distance between the two points
    return point_1.distance(point_2)
