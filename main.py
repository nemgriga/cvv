import requests
from html import _html5
# from render import render_template

STOCK = "GOOG"
COMPANY_NAME = "Alphabet Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "CXP8LJII14BBZV4E"
NEWS_API_KEY = "b8234aa6eca040abaf4e32b5d17bc6e1"
TWILIO_SID = "AC5cc49290695bba61ad72e16db3b74895"
TWILIO_AUTH_TOKEN = "8b5abbc89d45f1a93fc49872c67c1bbc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)


STOCK2 = "GOLD"
COMPANY_NAME2 = "Barrick Gold Corporation"

stock_params2 = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK2,
    "apikey": STOCK_API_KEY,
}

response2 = requests.get(STOCK_ENDPOINT, params=stock_params2)

data2 = response2.json()["Time Series (Daily)"]
data_list2 = [value2 for (key2, value2) in data2.items()]
yesterday_data2 = data_list2[0]
yesterday_closing_price2 = yesterday_data2["4. close"]
print(yesterday_closing_price2)

import bs4

# load the file
with open("existing_file.html") as inf:
    txt = inf.read()
    soup = bs4.BeautifulSoup(yesterday_closing_price, features="html.parser")
    soup2 = bs4.BeautifulSoup(yesterday_closing_price2, features="html.parser")

# create new link
new_link = soup.new_tag("link", rel="icon", type="image/png", href="img/tor.png")

with open("existing_file.html", "w") as outf:
    outf.write(str(f"<h1>Alphabet Inc. price is: {soup}</h1>\n"
                   f"<h1>Gold price is: {soup2}</h1>\n"
                   f"<img src='https://interactive-examples.mdn.mozilla.net/media/cc0-images/grapefruit-slice-332-332.jpg' alt='Grape fruit slice picture'>"))