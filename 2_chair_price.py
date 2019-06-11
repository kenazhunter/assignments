import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.ebay.com/itm/Garmin-eTrex-20x-Handheld-GPS-Receiver/173922297153")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"class": "notranslate", "id": "prcIsum", "itemprop": "price", "style":"", "content":"119.94" })
string_price = (element.text.strip())

price_without_symbol = string_price[4:]

price = (float(price_without_symbol))

if price < 200:
    print("Buy the Item")
    print("The current price is {}".format(price))
else:
    print("Too expensive, do not buy the item")

# <span class="notranslate" id="prcIsum" itemprop="price" style="" content="119.94">US $119.94</span>
