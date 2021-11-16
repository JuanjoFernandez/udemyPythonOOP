from config import api_key
import requests
import pandas as pd
from pprint import pprint

class NewsFeed:

    def __init__(self, data):
        self.data = data
    
    def get(self):
        pass

people = pd.read_excel('people.xlsx', usecols="A:D")
people.dropna(inplace=True)

# API call
url = 'https://newsapi.org/v2/everything?' \
      'qInTitle=apple&' \
      'from=2021-11-15&to=2021-11-15&sortBy=popularity&'
request = requests.get(url + 'apiKey=' + api_key)
response = request.json()
articles = response['articles']
news = []
for article in articles:
    art = (article['title'], article['url'])
    news.append(art)
for _ in news:
    print(_)


