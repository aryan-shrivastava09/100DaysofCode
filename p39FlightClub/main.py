from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

dm = DataManager()
sheety_data = dm.data
for d in sheety_data:
    if d["iataCode"] == "":
        f = FlightSearch(d)
pprint(sheety_data)
for d in sheety_data:
    iata = d["iataCode"]
    fd = FlightData(iata)
    print(f"{fd.city_to}:{fd.price}")
    if fd.price < d["lowestPrice"]:
        message = f"Price: {fd.price}\nDeparture City Name: {fd.departure_city}\nDeparture Airport IATA code: {fd.departure_airport}\nArrival City Name: {fd.city_to}\nArrival airport IATA code: {fd.arrival_airport}\nOutbound Date: {fd.outbound}\nInbound Date: {fd.inbound}"
        nm = NotificationManager(message)



        
