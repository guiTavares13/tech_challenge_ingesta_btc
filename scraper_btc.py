import requests
from bs4 import BeautifulSoup

class Scraper:
    
    def __init__(self, url):
        self.url = url

    def scrape(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')

        price = soup.find('div', attrs={
            'class': 'BNeawe iBp4i AP7Wnd'
        }).text

        return price