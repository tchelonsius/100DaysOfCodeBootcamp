import requests
import datetime
import config

"""-------------- GLOBAL VARIABLES --------------"""

API_KEY = config.API_KEY
API_SECRET = config.API_SECRET
TOKEN = ""
STANDARD_ENDPOINT = config.STANDARD_ENDPOINT
TOKEN_HEADER = config.TOKEN_HEADER
AUTHO_PARAMS = config.AUTHO_PARAMS
HEADER = config.HEADER


"""------------- CLASS DEFINITION -------------"""

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        global TOKEN
        response = requests.post(url='https://test.api.amadeus.com/v1/security/oauth2/token', headers=TOKEN_HEADER,
                                 data=AUTHO_PARAMS)
        TOKEN = response.json()['access_token']
        HEADER['Authorization'] = "Bearer "+TOKEN

    def set_params(self, origin: str, destination: str, date: datetime.date, max_price: int):
        params = {
            "originLocationCode": origin,
            "destinationLocationCode": destination,
            "departureDate": date,
            "adults": 1,
            "maxPrice": max_price,
            "currencyCode": "USD",
            "travelClass": "ECONOMY"
        }
        return params

    def get_data(self, params):
        response = requests.get("https://test.api.amadeus.com/v2/shopping/flight-offers", headers=HEADER, params=params)
        return response.json()


