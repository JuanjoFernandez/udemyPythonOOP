import requests
from selectorlib import Extractor
from temperature import Temperature


"""Stores input data and calculates daily calorie intake"""

class Calorie:
    def __init__(self, weight, height, age, temperature):
        self.weight = float(weight)
        self.height = float(height)
        self.age = float(age)
        self.temperature = float(temperature)

    def calculate(self):
        result = 10 * self.weight + 6.5 * self.height + 5 - self.temperature * 10
        return result