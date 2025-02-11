#This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
import key
import requests
import json
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch

dm = DataManager()
fs = FlightSearch
auth_url = "https://test.api.amadeus.com/v1/security/oauth2/token"

auth_params = {
                "grant_type":"client_credentials",
                "client_id": key.ama_client_id,
                "client_secret": key.ama_client_secret,
                }

auth_response = requests.post(auth_url, data=auth_params)

auth_response_token = auth_response.json()['access_token']
print(auth_response_token)


def get_flight_data():

    base_url = 'https://test.api.amadeus.com/v2/shopping/flight-offers'

    params = {"adults": 1,
              "departureDate": "2025-02-24",
              "destinationLocationCode": "LHR",
              "originLocationCode": "MIA",
              "nonStop": "true"

             }

    header = {
        "Authorization": f"Bearer {auth_response_token}"
    }

    flights = requests.get(base_url, headers=header, params=params)
    flight_json = flights.json()
    print(type(flight_json))
    #use this to be able to view the json in a json viewer.
    j = json.dumps(flight_json)
    print(j)

sheet_data = dm.get_all_data()
pprint(sheet_data)





