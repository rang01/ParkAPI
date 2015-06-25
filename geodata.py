import os
import json

cities_path = os.path.dirname(os.path.realpath(__file__))


def from_feature(feature):
    name = feature['properties']['name']
    lon, lat = feature['geometry']['coordinates']
    return name, {'lng': lon, 'lat': lat}


class GeoData:
    def __init__(self, city):
        json_path = os.path.join(cities_path, "cities", city + ".geojson")
        try:
            with open(json_path) as f:
                geodata = json.load(f)
                self.lots = dict(map(from_feature, geodata['features']))
        except FileNotFoundError:
            geodata = self.lots = {}

    def coords(self, lot):
        return self.lots.get(lot, None)