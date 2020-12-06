import requests
import json
import os
from dotenv import load_dotenv

# Load Env variables
load_dotenv()

# Define Constants
API_Key = os.getenv("API_Key")
BASE_URL = "https://financialmodelingprep.com/api/v3/"
SCREENER = f"stock-screener?&exchange=NYSE,NASDAQ&marketCapLowerThan=2000000000{API_Key}"

# Get request to JSON API
response = requests.get(f"{BASE_URL}{SCREENER}")
tickers = response.json()

# Filtered list
filtered_tickers = []

# List of sectors
sector_list = ["Technology", "Consumer Defensive",
               "Communication Services", "Healthcare", "Services"]

# Filter Results
for ticker in tickers:
    if ticker["price"] < 20.00 and ticker["price"] > 0.01 and ticker["marketCap"] > 0:
        if ticker["volume"] > 50000:
            for sector in sector_list:
                if ticker["sector"] == sector:
                    filtered_tickers.append(ticker)
                    continue

# Delete old file
if os.path.exists("screen.json"):
    os.remove("screen.json")

# Write Results to File
with open('screen.json', 'w') as filehandle:
    json.dump(filtered_tickers, filehandle)
