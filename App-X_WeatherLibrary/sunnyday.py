from config import API_key
import requests
from pprint import pprint

class Weather:

    def __init__(self, apikey, city=None, lat=None, lon=None):
        
        if city:
            url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={apikey}&units=imperial"
            r = requests.get(url)
            self.data = r.json()
        elif lat and lon:
            url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&APPID={apikey}&units=imperial"
            r = requests.get(url)
            self.data = r.json()
        else:
            raise TypeError("provide either a city or lat and lon arguments")
    
    def next_12h(self):
        return self.data['list'][:4]

    def next_12h_simplified(self):
        pass

weather = Weather(apikey=API_key, city="Madrid", lat=4.1, lon=4.5)
pprint(weather.next_12h())