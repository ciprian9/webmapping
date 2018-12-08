import pyproj as proj
from shapely import geometry

def distance_checker(lat, lon, check_lat, check_lon, shapely=None):
    crs_wgs = proj.Proj(init='epsg:4326')
    crs_bng = proj.Proj(init='epsg:27700')
    x1, y1 = proj.transform(crs_wgs, crs_bng, lon, lat)
    x2, y2 = proj.transform(crs.wgs, crs_bng, check_lon, check_lat)
    point_1 = geometry.Point(x1, y1)
    point_2 = geometry.Point(x2, y2)
    return point_1.distance(point_2)
