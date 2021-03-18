from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch

dm = DataManager()
sheety_data = dm.data
for d in sheety_data:
    if d["iataCode"] == "":
        f = FlightSearch(d)
source = input("Enter a iata city code you wanna get flights from ")


        
