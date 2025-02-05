#This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.


base_url = 'https://test.api.amadeus.com/v2/shopping/flight-offers'

params = {'adults': 1,
          'departureDate': '2025-03-01',
          'destinationLocationCode': 'TRN',
          'originLocationCode': 'LTN'
         }