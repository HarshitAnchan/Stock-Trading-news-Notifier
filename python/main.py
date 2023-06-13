import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = ""
NEWS_API_KEY = ""
TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""


stock_params={
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK_NAME,
    "interval": "60min",
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (60min)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)


day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)


difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)

diff_percent = (difference / float(yesterday_closing_price)) * 100
print(diff_percent)




if diff_percent > 0.01:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,

    }
    news_response  = requests.get(NEWS_ENDPOINT, params= news_params)
    articles = news_response.json()["articles"]
    print(articles)




three_articles = articles[:3]
print(three_articles)
   

formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]



client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

for article in formatted_articles:
    message = client.messages.create(
        from_='+13613043590',
        body=article,
        to='YOUR PHONE NO.'
    )


