# Day 35: rain alert
#
# This program is run at the beginning of each day
# using PythonAnywhere. It uses the openweathermap
# API to check whether it is going to rain in a
# certain location in the next 12 hours. If that's
# the case, a sms is sent to the phone number provided
# using the twilio api, informing about the rainy forecast.

import config
import requests
from twilio.rest import Client

account_sid = config.ACCOUNT_SID
auth_token = config.AUTH_TOKEN
client = Client(account_sid, auth_token)

def send_message():
    message = client.messages.create(
      from_=config.VIRTUAL_NUMBER,
      body='it will rain in the next 12 hours.',
      to=config.MY_NUMBER
    )
    print(message.status)


AMOUNT = 4

parameters = {
    "lat": -22.906847,
    "lon": -43.172897,
    "appid": config.APPID_KEY,
    "cnt": AMOUNT
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", parameters)
data = response.json()

for f in range(AMOUNT):
    print(f"time: {data['list'][f]['dt_txt']}")
    condition_code = data['list'][f]['weather'][0]["id"]
    if condition_code < 700:
        send_message()
        break


