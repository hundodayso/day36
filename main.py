#This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
import key
import requests
import json
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
SHEETY_PRICES_ENDPOINT = key.sheet_data_ep

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

#sheet_data = [{'city': 'Paris', 'iataCode': '', 'id': 2, 'lowestPrice': 54},
 # {'city': 'Frankfurt', 'iataCode': '', 'id': 3, 'lowestPrice': 42},
 # {'city': 'Tokyo', 'iataCode': '', 'id': 4, 'lowestPrice': 485},
 # {'city': 'Hong Kong', 'iataCode': '', 'id': 5, 'lowestPrice': 551},
 # {'city': 'Istanbul', 'iataCode': '', 'id': 6, 'lowestPrice': 95},
 # {'city': 'Kuala Lumpur', 'iataCode': '', 'id': 7, 'lowestPrice': 414},
 # {'city': 'New York', 'iataCode': '', 'id': 8, 'lowestPrice': 240},
 # {'city': 'San Francisco', 'iataCode': '', 'id': 9, 'lowestPrice': 260},
 # {'city': 'Dublin', 'iataCode': '', 'id': 10, 'lowestPrice': 378},
 # {'city': 'Turin', 'iataCode': '', 'id': 11, 'lowestPrice': 80}]
sheet_data = dm.get_all_data()
pprint(sheet_data)
dm.update_destination_codes()



####Trying
# sheety_header = {
#     "Authorization": key.sheety_token
# }

# for city in sheet_data:
#     id = city['id']
#     print(id)
#     sheet_update_ep = f"{SHEETY_PRICES_ENDPOINT}/{id}"
#     new_data = {
#         "price":{
#             "iataCode": "TESTING"
#         }
#     }
#     response = requests.put(url=sheet_update_ep, headers=sheety_header, json=new_data)
#     print(response)





