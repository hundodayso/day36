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
        self.data = response.json()
        return self.data['prices']


