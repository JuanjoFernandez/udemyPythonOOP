import requests
from selectorlib import Extractor


class Temperature:
    """Scraps city temperature from timeanddate.com"""
    def __init__(self, country, city):
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def get(self):
        url = f'https://www.timeanddate.com/weather/{self.country}/{self.city}'
        request = requests.get(url)
        text = request.text
        extractor = Extractor.from_yaml_file('temperature.yaml')
        raw = extractor.extract(text)
        temperature = float(raw['temp'].replace('\xa0°F', ""))
        
        # Making sure temperature is in Celsius
        if raw['temp'].find("F"):
            temperature = (temperature - 32) / 1.8
        
        return temperature
