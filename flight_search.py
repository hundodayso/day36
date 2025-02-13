import requests
import key
import json
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
            "keyword": f"{city_name}"
        }
        return code

    def _get_new_token(self):
        auth_url = "https://test.api.amadeus.com/v1/security/oauth2/token"

        auth_params = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }

        auth_response = requests.post(auth_url, data=auth_params)
        self.auth_response_token = auth_response.json()['access_token']
        return self.auth_response_token
    def get_flight_data_offers(self):
        base_url = 'https://test.api.amadeus.com/v2/shopping/flight-offers'
        params = {"adults": 1,
                  "departureDate": "2025-02-24",
                  "destinationLocationCode": "LHR",
                  "originLocationCode": "MIA",
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
