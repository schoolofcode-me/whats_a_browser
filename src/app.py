__author__ = 'jslvtr'

import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.johnlewis.com/store/john-lewis-wade-office-chair-black/p447855")
soup = BeautifulSoup(r.content, "html.parser")
element = soup.find("span", {"itemprop": "price", "class": "now-price"})
string_value = element.text.strip() #"£115.00"

price = float(string_value[1:])

if price < 100:
    print("Buy the chair!")
elif price == 100:
    print("Buy at your own peril!")
else:
    print("Definitely don't buy.")

# <span itemprop="price" class="now-price"> £115.00 </span>
