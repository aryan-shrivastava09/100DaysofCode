import requests
API_KEY = "pOXc739oOCAZeG1CdCxXa8O-YzWT4xgk"
API_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, d):
        self.cityrow = d
        self.GETIATA()
        
    def GETIATA(self):
        headers = {
            "apikey" : API_KEY
        }
        params = {
            "term" : str(self.cityrow["city"]),
            "locale":"en-US",
            "location-types": "city",
            "limit":1,
            "active_only":True
        }
        response = requests.get(url= API_ENDPOINT, params= params, headers = headers)
        response.raise_for_status()
        data = response.json()
        self.iatacode = data["locations"][0]["code"]
        self.updateiata()
    
    def updateiata(self):
        self.cityrow["iataCode"] = self.iatacode

        