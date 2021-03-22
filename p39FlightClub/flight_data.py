from datetime import datetime, timedelta
import requests

API_KEY = "pOXc739oOCAZeG1CdCxXa8O-YzWT4xgk"
API_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
DATE_FROM = datetime.now().strftime("%d/%m/%Y")
DATE_TO = (datetime.now() + timedelta(days= 6 * 30)).strftime("%d/%m/%Y")
class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,d):
        self.fly_to = d
        headers = {
            "apikey" : API_KEY 
        }
        params = {
            "fly_from" : "city:LON",
            "fly_to" : self.fly_to,
            "date_from" : DATE_FROM,
            "date_to": DATE_TO,
            "nights_in_dst_from" : 7,
            "nights_in_dst_to" : 28,
            "curr" : "GBP"
        }
        response = requests.get(API_ENDPOINT, headers = headers, params= params)
        response.raise_for_status()
        self.data = response.json()["data"]
        self.city_to = self.data[0]["cityTo"]
        self.price = self.data[0]["price"]
        self.mailinfo()

        def mailinfo(self):
            self.departure_city = self.data[0]["cityFrom"]
            self.departure_airport = self.data[0]["flyFrom"]
            self.arrival_airport = self.data[0]["flyTo"]
            self.outbound = self.data[0]["route"][0]["local_departure"]
            self.inbound = self.data[0]["route"][1]["local_departure"]

