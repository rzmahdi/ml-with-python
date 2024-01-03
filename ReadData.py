import requests
from bs4 import BeautifulSoup
import sql

# split comma in string
def spliter(string:str):
    if ',' in string:
        return "".join(string.split(','))
    else:
        return string

# read data from truecar.com
for page in range(1, 333):
    url = f'https://www.truecar.com/used-cars-for-sale/listings/?page={page}'
    
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    print(page)
    # find all car cards in one page
    elements = soup.find_all('div', 'card-content')
    for card in elements:
        # Separator top part of the card for car model and production year
        top = card.find('div', 'vehicle-card-top').find('div', 'truncate')

        # spliting data
        year = top.find('span', 'vehicle-card-year').text
        model = top.find('span', 'truncate').text                                                  
        # split $ and comma -> $22,123 => 22123 
        price = spliter(card.find('div', 'vehicle-card-bottom-pricing').find('div', 'normal-case').text.split("$")[-1])
        mile_age = spliter(card.find('div', 'border-t').find('div', 'truncate').text.split()[0])
        # write data in DataBase
        sql.write(model, year, mile_age, price)