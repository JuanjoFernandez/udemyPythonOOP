import requests
from selectorlib import Extractor


class Temperature:
    """Scraps city temperature from timeanddate.com"""
    def __init__(self, country, city):
        self.country = country
        self.city = city

    def get(self):
        url = f'https://www.timeanddate.com/weather/{self.country}/{self.city}'
        request = requests.get(url)
        text = request.text
        extractor = Extractor.from_yaml_file('temperature.yaml')
        raw = extractor.extract(text)
        temperature = float(raw['temp'].replace('\xa0°F', ""))

        return temperature
