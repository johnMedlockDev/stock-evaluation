from classes.Account import Account
import requests
import json
import os


class Screener(Account):
    def __init__(self):
        # Get request to JSON API
        super().__init__()
        self.response = requests.get(
            f"{self.BASE_URL}{self.SCREENER}")
        self.tickers = self.response.json()
        # Filtered list
        self.filtered_tickers = []
        self.__filterResults()
        self.__persistResults()

    def __filterResults(self):
        # List of sectors
        sector_list = ["Technology", "Consumer Defensive",
                       "Communication Services", "Healthcare", "Services"]

        # Filter Results
        for ticker in self.tickers:
            if ticker["price"] < 20.00 and ticker["price"] > 0.01 and ticker["marketCap"] > 0:
                if ticker["volume"] > 50000:
                    for sector in sector_list:
                        if ticker["sector"] == sector:
                            self.filtered_tickers.append(ticker)
                            continue

    def __persistResults(self):
        # Delete old file
        if os.path.exists("./output/screen.json"):
            os.remove("./output/screen.json")

        # Write Results to File
        with open('./output/screen.json', 'w') as filehandle:
            json.dump(self.filtered_tickers, filehandle)
