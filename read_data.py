import requests
from bs4 import BeautifulSoup

# for i in range(1, 333):
data = requests.get('https://www.truecar.com/used-cars-for-sale/listings/?page=2')
soup = BeautifulSoup(data.text, 'html.parser')
cards = soup.find('div', 'card-content')
top = cards.find('div', 'vehicle-card-top').find('div', 'truncate')
price = cards.find('div', 'vehicle-card-bottom-pricing').find('div', 'normal-case').text

year = top.find('span', 'vehicle-card-year').text
car_name, model = top.find('span', 'truncate').text.split()
print(soup)