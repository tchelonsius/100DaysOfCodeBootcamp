from data_manager import *
from flight_data import *
from notification_manager import *
from datetime import date, timedelta


def daterange(start_date: date, end_date: date):
    days = int((end_date - start_date).days)
    for n in range(days):
        yield start_date + timedelta(n)

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.data_manager = DataManager()
        self.flight_data = FlightData()
        self.not_manager = NotificationManager()


    def search(self):
        today = datetime.date.today()
        for single_date in daterange(today+timedelta(7), today+timedelta(187)):
            for f in range(self.data_manager.items_amount):
                org = "GIG"
                dest = self.data_manager.codes_list[f]
                price = self.data_manager.prices_list[f]
                search_params = self.flight_data.set_params(org, dest, single_date, price)
                infos = self.flight_data.get_data(search_params)
                if infos['meta']['count']>0:
                    best_price = self.find_best_price(infos, float(price))
                    print(f"Data for date {single_date}:\n{infos}")
                    message = f"A flight from GIG - Rio de Janeiro to {dest} - {self.data_manager.cities_list[f]} on {str(single_date)} was found for {best_price:.2f}$."
                    self.not_manager.send_email(message)
                else:
                    print(f"No flights were found to {dest}.")

    def find_best_price(self, info: dict, price):
        best_price = price
        for flight in info['data']:
            if float(flight['price']['grandTotal']) < best_price:
                best_price = float(flight['price']['grandTotal'])
        return best_price





