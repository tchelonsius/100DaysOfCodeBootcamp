import requests
from datetime import datetime
import info
from requests.auth import HTTPBasicAuth

today = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# natural language api infos
APP_ID = info.APP_ID
API_KEY = info.API_KEY
host_domain = "https://trackapi.nutritionix.com"
exercise_endpoint = "/v2/natural/exercise"

# google sheets editor data
get_data_endpoint = info.get_data_endpoint
post_data_endpoint = info.post_data_endpoint
authorization_key = info.authorization_key
basic = HTTPBasicAuth(info.username, info.psw)


headers = {
    "x-app-key": API_KEY,
    "x-app-id": APP_ID

}

query = input("what exercises have you done today? ")

request_params = {
    "query": query,
    "weight_kg": 85,
    "height_cm": 184.0,
    "age": 20
}

response = requests.post(host_domain+exercise_endpoint, json=request_params, headers=headers)

answer = response.json()["exercises"][0]

body = {
    "workout": {
        "date": today,
        "time": now_time,
        "exercise": answer["name"].title(),
        "duration": answer["duration_min"],
        "calories": answer["nf_calories"]

    }
}


response = requests.post(post_data_endpoint, json=body, auth=basic)




