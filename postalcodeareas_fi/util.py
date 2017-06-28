from geojson import Feature, Point, FeatureCollection, dumps
from shapely.geometry import asPolygon

from .data import areas, centers


def polygon_center(polygon_coordinates):
   "return polygon centroid"
   centroid = asPolygon(polygon_coordinates).centroid
   return ("%.6f" % centroid.x, "%.6f" % centroid.y)

def geojson_areas(data=areas, dump=True):
   "generate areas in geojson format"
   features = []
   for area, boundary in data.items():
      p = Poly(boundary)
      f = Feature(geometry=p, properties={"postalcode":area})
      features.append(f)
   collection = FeatureCollection(features)
   return collection if not dump else dumps(collection, sort_keys=True)

def geojson_centers(data=centers, dump=True):
   "generate centers in geojson format"
   features = []
   for area, center in data.items():
      p = Point(center)
      f = Feature(geometry=p, properties={"postalcode":area})
      features.append(f)
   collection = FeatureCollection(features)
   return collection if not dump else dumps(collection, sort_keys=True)
