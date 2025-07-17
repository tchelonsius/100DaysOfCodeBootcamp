# This project uses the pixela web server to
# keep track on habit results. Graphs similar
# to those used in github can be created,
# edited, deleted. The main goal was to practice
# different ways to interact with an api, by
# using methods like get, post, put and delete.

import requests
from datetime import datetime
import info

USERNAME = info.username
TOKEN = info.token
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = info.graph_id

now = datetime.now()
TODAY = now.strftime("%Y%m%d")


creation_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}


# response = requests.post(url=pixela_endpoint, json=creation_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": GRAPH_ID,
    "name": "reading graph",
    "unit": "pages",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}


# response = requests.post(graph_endpoint, json=graph_params, headers=headers)
# print(response.json)


pixel_params = {
    "date": TODAY,
    "quantity": "30"
}
pixel_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# response = requests.post(pixel_post_endpoint, json=pixel_params, headers=headers)
# print(response.text)

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"
response = requests.delete(pixel_delete_endpoint, headers=headers)
print(response.text)

