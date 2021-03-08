import requests
import datetime as dt
response = requests.get(url = "http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)
print(iss_position)


parameters = {
    "lat": 27.176670,
    "lng": 78.008072,
    "formatted":0
}

response1 = requests.get(url = "https://api.sunrise-sunset.org/json", params= parameters)
response1.raise_for_status()
data1 = response1.json()
sunrise = (data1["results"]["sunrise"].split("T")[1]).split(":")[0]
sunset = (data1["results"]["sunset"].split("T")[1]).split(":")[0]
risesetTime = (sunrise,sunset)
print(risesetTime)
nowtime = str(dt.datetime.now()).split()[1].split(":")[0]
print(nowtime)
difftime = int(nowtime) - int(sunrise)
print(difftime)