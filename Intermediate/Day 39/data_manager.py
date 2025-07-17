from requests.auth import HTTPBasicAuth
import requests
import config

"""-------------- GLOBAL VARIABLES --------------"""

authorization_key = config.AUTHORIZATION_KEY
basic = HTTPBasicAuth(config.USERNAME,config.PSW)
url = config.URL

"""------------- CLASS DEFINITION -------------"""

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.response = requests.get(url, auth=basic)
        self.values = self.response.json()
        self.items_amount = len(self.values['prices'])
        self.prices_list = [row['lowestPrice'] for row in self.values['prices']]
        self.codes_list = [row['iataCode'] for row in self.values['prices']]
        self.cities_list = [row['city'] for row in self.values['prices']]


