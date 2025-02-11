import key
import requests

SHEETY_PRICES_ENDPOINT = key.sheet_data_ep
class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self._token = key.sheety_token


    def get_all_data(self):
        sheety_header = {
            "Authorization": key.sheety_token
        }
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=sheety_header)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
        pass


