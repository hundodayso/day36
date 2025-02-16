import requests
import key
import json
import time
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.client_id = key.ama_client_id
        self.client_secret = key.ama_client_secret
        self._token = self._get_new_token()


    def get_destination_code(self, city_name):
        code = "TESTING"
        url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        params = {
            "keyword": f"{city_name}",
            "include": "AIRPORTS"
        }

        header = {
            "Authorization": f"Bearer {self._token}"
        }

        response = requests.get(url=url, headers=header, json=params)
        print(response.json)
        return code

    def _get_new_token(self):
        TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

        auth_params = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }

        auth_response = requests.post(url=TOKEN_ENDPOINT, data=auth_params)
        self.auth_response_token = auth_response.json()['access_token']
        return self.auth_response_token
    def check_flights(self, departure_city_code, destination_city_code, from_date, to_date):
        base_url = 'https://test.api.amadeus.com/v2/shopping/flight-offers'
        params = {"adults": 1,
                  "departureDate": from_date.strftime("%Y-%m-%d"),
                  "returnDate": to_date.strftime("%Y-%m-%d"),
                  "destinationLocationCode": destination_city_code,
                  "originLocationCode": departure_city_code,
                  "currencyCode": "GBP",
                  "nonStop": "true"
                  }

        header = {
            "Authorization": f"Bearer {self._token}"
        }

        flights = requests.get(base_url, headers=header, params=params)
        flight_json = flights.json()
        print(type(flight_json))
        # use this to be able to view the json in a json viewer.
        j = json.dumps(flight_json)
        print(j)
        return flight_json
