from config import api_key
import requests

class NewsFeed:
    """Representing multiple news and links as a single string"""

    base_url = 'https://newsapi.org/v2/everything?'
    def __init__(self, interest, from_date, to_date, language='en'):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language
    
    def get(self):
        url = self._build_url()
        
        articles = self._get_articles(url)

        email_body = ''
        for article in articles:
            email_body = email_body +  article['title'] + '\n' + article['url'] + '\n\n'

        return(email_body)

    def _get_articles(self, url):
        request = requests.get(url)
        response = request.json()
        articles = response['articles']
        return articles
    
    def _build_url(self):
        url = f'https://newsapi.org/v2/everything?' \
              f'qInTitle={self.interest}&' \
              f'from={self.from_date}&to={self.to_date}&' \
              f'language={self.language}&'\
              f'apiKey={api_key}'
        return url






