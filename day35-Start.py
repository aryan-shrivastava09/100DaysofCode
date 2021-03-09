import requests
# import os
# from twilio.rest import Client
# import smtplib

apikey = "004cede7c783de4f31409837a9473f72"
# account_sid = 'AC3a659cf35304756765ca4505ffaae000'
# auth_token = '8746c90689ba198da099c56b80cc7921'
# my_email = "aryans009"
parameters = {
    "lat": -9.973870,
    "lon": -67.807541,
    "exclude":"current,minutely,daily,alerts",
    "appid":apikey
}
response = requests.get(url=  "https://api.openweathermap.org/data/2.5/onecall" , params= parameters)
response.raise_for_status()
data = response.json()["hourly"]
weatherslice = data[:12]
flag =False
for w in weatherslice:
    weather = w["weather"][0]
    condition_id = weather["id"]
    print(condition_id)
    if int(condition_id) < 700:
        flag = True

if flag == True:
    # client = Client(account_sid, auth_token)

    # message = client.messages.create(
    #                     body="Bring an Umbrella",
    #                     from_='+18186433543',
    #                     to='+919410205099'
    #                 )

    # print(message.status)
    print("umbrella")
    # connection = smtplib.SMTP(url = "smtp.gmail.com")
    
