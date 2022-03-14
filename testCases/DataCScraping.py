import requests
from bs4 import BeautifulSoup


source = requests.get('https://en.wikipedia.org/wiki/Lists_of_cities')
source.raise_for_status()

soup = BeautifulSoup(source.text,'html.parser')
print(soup)


