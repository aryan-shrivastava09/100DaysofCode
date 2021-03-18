import requests
from pprint import pprint

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_endpoint_get = "https://api.sheety.co/b97bf893bfb25d8ddd9a3cbee3a19644/copyOfFlightDeals/prices"
        response = requests.get(url = self.sheety_endpoint_get)
        self.data = response.json()["prices"]

