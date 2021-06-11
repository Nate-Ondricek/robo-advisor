print("TODO: make a web request for some stock market data")

#first read env variables

# This is the URL we want to use: https://www.alphavantage.co/documentation/#dailyadj

import os
from dotenv import load_dotenv
import requests
load_dotenv() # go get env vars from the .env file

# read env variables
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

# make a request
symbol = "MSFT" # ask for a user input
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"
response = requests.get(request_url)
print(type(response))
print(response.text)
