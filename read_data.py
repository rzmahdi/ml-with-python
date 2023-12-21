import requests
from bs4 import BeautifulSoup

# split comma in string
def spliter(string:str):
    if ',' in string:
        return int("".join(string.split(',')))
    else:
        return int(string)

# read data from truecar.com
def read_data():
    for page in range(1, 333):
        url = f'https://www.truecar.com/used-cars-for-sale/listings/?page={page}'
        
        data = requests.get(url)
        soup = BeautifulSoup(data.text, 'html.parser')
        
        # find all car cards in one page
        elements = soup.find_all('div', 'card-content')
        
        for card in elements:
            # Separator top part of the card for car model and production year
            top = card.find('div', 'vehicle-card-top').find('div', 'truncate')

            # production year
            year = int(top.find('span', 'vehicle-card-year').text)
            # car model
            model = top.find('span', 'truncate').text
            price = spliter(card.find('div', 'vehicle-card-bottom-pricing').find('div', 'normal-case').text.split("$")[-1])
            mile_age = spliter(card.find('div', 'border-t').find('div', 'truncate').text.split()[0])

            return model, year, mile_age, price