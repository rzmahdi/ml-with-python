import requests
from bs4 import BeautifulSoup

# split comma in string
def spliter(string:str):
    if ',' in string:
        return int("".join(string.split(',')))
    else:
        return int(string)

# read data from truecar.com
for i in range(1, 333):
    data = requests.get(f'https://www.truecar.com/used-cars-for-sale/listings/?page={i}')
    soup = BeautifulSoup(data.text, 'html.parser')
    
    cards = soup.find('div', 'card-content')
    top = cards.find('div', 'vehicle-card-top').find('div', 'truncate')

    year = int(top.find('span', 'vehicle-card-year').text)
    car_name, model = top.find('span', 'truncate').text.split()
    price = spliter(cards.find('div', 'vehicle-card-bottom-pricing').find('div', 'normal-case').text.split("$")[-1])
    mile_age = spliter(cards.find('div', 'border-t').find('div', 'truncate').text.split()[0])