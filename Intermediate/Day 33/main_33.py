# This program checks every 60 seconds if the International
# Space Station is close to my current position in latitude
# and longitude. When that's the case, an email will be sent
# to me to look up to the sky and try to find it.
# This project was done using the ISS api that provides the
# data needed.

import requests
import time
import smtplib
import info

MY_LAT = info.lat
MY_LONG = info.long
MY_EMAIL = info.email
MY_PSW = info.psw


while True:
    response = requests.get("http://api.open-notify.org/iss-now.json")
    iss_latitude = float(response.json()["iss_position"]["latitude"])
    iss_longitude = float(response.json()["iss_position"]["longitude"])

    print(f"lat, long: ({iss_latitude}, {iss_longitude})")

    message = (f"Subject: International Space Station close\n\n"
               f"ISS is getting closer.\n"
               f"Current position: latitude: {iss_latitude}, longitude: {iss_longitude}")

    if abs(iss_latitude - MY_LAT) < 5 and abs(iss_longitude - MY_LONG) < 5:
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.startlls()
        connection.login(user=MY_EMAIL, password=MY_PSW)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=message)
        connection.close()
    time.sleep(60)