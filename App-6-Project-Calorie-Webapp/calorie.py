import requests
from selectorlib import Extractor
from temperature import Temperature


"""Stores input data and calculates daily calorie intake"""

class Calorie:
    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        pass
