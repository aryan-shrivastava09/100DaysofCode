import requests
import smtplib

MY_EMAIL = "aryansri009@gmail.com"
MY_PASSWORD = "Prioryofsion09"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_APIKEY = "8YY9KKHNJD9MTCGD"
NEWS_APIKEY = "89154282b5ac45bc8c2b384e16ba6c99"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
YES_DATE = "2021-03-08"
TODAY_DATE = "2021-03-09"

parameters_stock = {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_APIKEY
}

parameters_news = {
    "q": COMPANY_NAME,
    "from": TODAY_DATE,
    "to": TODAY_DATE,
    "sortBy":"popularity",
    "apikey" : NEWS_APIKEY
}

message = []

response = requests.get(url=STOCK_ENDPOINT,params= parameters_stock)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
yes_data_close = float(data[YES_DATE]["4. close"])
today_data_open = float(data[TODAY_DATE]["1. open"])

if abs(today_data_open - yes_data_close) > 0:
    diff = today_data_open - yes_data_close
    response2 = requests.get(url= NEWS_ENDPOINT, params= parameters_news)
    response2.raise_for_status()
    data2 = response2.json()["articles"][:3]
    if diff>0:
        header = (f"TSLA : UP {round(diff/yes_data_close*100)}%\n")
    elif diff<0:
        diff = -diff
        header = (f"TSLA: DOWN {round(diff/yes_data_close*100)}%\n")
    
    for data in data2:
        title = data["title"]
        description = data["description"]
        url = data["url"]
        message = header + (f"Headline : {title}\nBrief : {description}\nURL : {url}\n\n")
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user= MY_EMAIL, password= MY_PASSWORD)
        connection.sendmail(from_addr= MY_EMAIL, to_addrs= "aryan.shrivastava9@gmail.com", msg= f"Subject:Stock News\n\n{message}")
    
    connection.close()

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

