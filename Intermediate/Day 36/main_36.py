# In this project, the two last closing prices of
# Tesla's stock is requested from the alpha vantage API. The program
# calculates the price variation in percentage between these two days
# and requests news about this company from the news API,
# creates a message containing these news and sends it by email.



import requests
import config
import smtplib
import email.message
import datetime


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
URL = "https://www.alphavantage.co/query?"
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": config.ALPHAVANTAGE_API_KEY
}

# sends the email with the given message to the given email
def send_email(emails_list: list, message: str):
    my_email = config.MY_EMAIL
    password = config.EMAIL_PSW

    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.ehlo()
    connection.starttls()
    connection.login(user=my_email, password=password)
    for address in emails_list:
        connection.sendmail(from_addr=my_email, to_addrs=address, msg=message)
    connection.close()


def create_message_and_send(dif: float, increased: bool):
    NEWSAPI_URL = "https://newsapi.org/v2/everything?"
    news_parameters = {
        "apiKey": config.NEWSAPI_KEY,
        "from": datetime.date,
        "sortBy": "relevancy",
        "q": "tesla stock's price"
    }

    news_response = requests.get(NEWSAPI_URL, news_parameters)
    print(news_response.json())
    articles_list = news_response.json()["articles"]
    to_send = ""
    if increased:
        to_send += "Subject: TSLA: 🔺"+ f"{dif:.2f}" +"%\n\n"
    else:
        to_send += "Subject: TSLA: 🔻" + f"{dif:.2f}" + "%\n\n"
    for article in articles_list:
        to_send += article["title"] + "\n"
        to_send += article["description"] + "\n"
        to_send += article["url"] + "\n"
        to_send += "\n"

    print(to_send)
    email_addresses = [config.TO_SEND_1, config.TO_SEND_2]
    send_email(email_addresses, to_send.encode('utf-8'))




# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stocks_response = requests.get(URL, stock_parameters)
data = stocks_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday = float(data_list[0]['4. close'])
before_yesterday = float(data_list[1]['4. close'])
print(f"yesterday: {yesterday}")
print(f"before yesterday: {before_yesterday}")
difference = 100*abs(before_yesterday-yesterday)/yesterday

print(difference)
if before_yesterday>yesterday:
    print(f"decrease of {difference:.2f}%")
    create_message_and_send(dif=difference, increased=False)
else:
    print(f"increase of {difference:.2f}%")
    create_message_and_send(dif=difference, increased=True)






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
