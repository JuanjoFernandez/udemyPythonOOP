from config import API_key
import requests
from pprint import pprint

class Weather:
    """Creates a weather object gatting an apikey as input and either a city name or lat and lon coordinates.

    Package use example:

    # Create a weather object using a city name:
    # You need to obtain an API key from: https://openweathermap.org
    # After registering and obtaining your API key it can take up to two hours to be active

    >>> weather1 = Weather(apikey = "your API key", city = "Madrid")

    # Using latitude and longitude coordinates
    >>> weahter2 = Weather(apikey = "your API key", lat = 41.1, lon = -4.1)

    # Get complete weather data for the next 12 hours:
    >>> weather1.next_12h()

    # Simplified data for the next 12 hours:
    >>> weather1.next_12h_simplified()
    
    """
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

        if self.data['cod'] != '200':
            raise ValueError(self.data['message'])
    
    def next_12h(self):
        """ Returns 3-hour data for the next 12 hours as a dict.
        """
        return self.data['list'][:4]

    def next_12h_simplified(self):
        """ Returns date, temperature, and sky condition every 3 hours for the next
            12 hours as a tuple of tuples.
        """
        simple_data = []
        for time in self.data['list'][:4]:
            simple_data.append((time['dt_txt'], time['main']['temp'], time['weather'][0]['description']))
        
        return simple_data

weather = Weather(apikey=API_key, city="Madrid", lat=4.1, lon=4.5)
pprint(weather.next_12h_simplified())