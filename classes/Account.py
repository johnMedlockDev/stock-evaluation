import os
from dotenv import load_dotenv, main


class Account(object):

    def __init__(self):
        load_dotenv()
        self.API_Key = os.getenv("API_Key")
        self.BASE_URL = "https://financialmodelingprep.com/api/v3/"
        self.SCREENER = f"stock-screener?&exchange=NYSE,NASDAQ&marketCapLowerThan=2000000000{self.API_Key}"
