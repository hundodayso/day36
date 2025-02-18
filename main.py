#This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
import key
import requests
import json
import time
from datetime import datetime, timedelta
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
SHEETY_PRICES_ENDPOINT = key.sheet_data_ep
ORIGIN_CITY = "LON"

dm = DataManager()
fs = FlightSearch()
# auth_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
#
# auth_params = {
#                 "grant_type":"client_credentials",
#                 "client_id": key.ama_client_id,
#                 "client_secret": key.ama_client_secret,
#                 }
#
# auth_response = requests.post(auth_url, data=auth_params)
#
# auth_response_token = auth_response.json()['access_token']
# print(auth_response_token)


flights_output = r'''{
  "meta": {
    "count": 12,
    "links": {
      "self": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=LON&destinationLocationCode=CDG&departureDate=2025-02-17&returnDate=2025-08-16&adults=1&nonStop=true&currencyCode=GBP&max=250"
    }
  },
  "data": [
    {
      "type": "flight-offer",
      "id": "1",
      "source": "GDS",
      "instantTicketingRequired": false,
      "nonHomogeneous": false,
      "oneWay": false,
      "isUpsellOffer": false,
      "lastTicketingDate": "2025-02-17",
      "lastTicketingDateTime": "2025-02-17",
      "numberOfBookableSeats": 9,
      "itineraries": [
        {
          "duration": "PT1H20M",
          "segments": [
            {
              "departure": {
                "iataCode": "LHR",
                "terminal": "4",
                "at": "2025-02-17T11:30:00"
              },
              "arrival": {
                "iataCode": "CDG",
                "terminal": "2E",
                "at": "2025-02-17T13:50:00"
              },
              "carrierCode": "AF",
              "number": "1581",
              "aircraft": {
                "code": "223"
              },
              "operating": {
                "carrierCode": "AF"
              },
              "duration": "PT1H20M",
              "id": "2",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        },
        {
          "duration": "PT1H25M",
          "segments": [
            {
              "departure": {
                "iataCode": "CDG",
                "terminal": "2E",
                "at": "2025-08-16T07:35:00"
              },
              "arrival": {
                "iataCode": "LHR",
                "terminal": "4",
                "at": "2025-08-16T08:00:00"
              },
              "carrierCode": "AF",
              "number": "1680",
              "aircraft": {
                "code": "223"
              },
              "operating": {
                "carrierCode": "AF"
              },
              "duration": "PT1H25M",
              "id": "7",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        }
      ],
      "price": {
        "currency": "GBP",
        "total": "429.82",
        "base": "321.00",
        "fees": [
          {
            "amount": "0.00",
            "type": "SUPPLIER"
          },
          {
            "amount": "0.00",
            "type": "TICKETING"
          }
        ],
        "grandTotal": "429.82",
        "additionalServices": [
          {
            "amount": "87.60",
            "type": "CHECKED_BAGS"
          }
        ]
      },
      "pricingOptions": {
        "fareType": [
          "PUBLISHED"
        ],
        "includedCheckedBagsOnly": false
      },
      "validatingAirlineCodes": [
        "AF"
      ],
      "travelerPricings": [
        {
          "travelerId": "1",
          "fareOption": "STANDARD",
          "travelerType": "ADULT",
          "price": {
            "currency": "GBP",
            "total": "429.82",
            "base": "321.00"
          },
          "fareDetailsBySegment": [
            {
              "segmentId": "2",
              "cabin": "ECONOMY",
              "fareBasis": "TYS0AALA",
              "brandedFare": "LIGHT",
              "brandedFareLabel": "ECONOMY LIGHT",
              "class": "T",
              "includedCheckedBags": {
                "quantity": 0
              },
              "amenities": [
                {
                  "description": "CHECKED BAG 1PC OF 23KG 158CM",
                  "isChargeable": true,
                  "amenityType": "BAGGAGE",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SNACK",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "BEVERAGE",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SEAT SELECTION",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "MILEAGE ACCRUAL",
                  "isChargeable": false,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "UPGRADE ELIGIBILITY",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                }
              ]
            },
            {
              "segmentId": "7",
              "cabin": "ECONOMY",
              "fareBasis": "BYS0AALA",
              "brandedFare": "LIGHT",
              "brandedFareLabel": "ECONOMY LIGHT",
              "class": "B",
              "includedCheckedBags": {
                "quantity": 0
              },
              "amenities": [
                {
                  "description": "CHECKED BAG 1PC OF 23KG 158CM",
                  "isChargeable": true,
                  "amenityType": "BAGGAGE",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SNACK",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "BEVERAGE",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SEAT SELECTION",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "MILEAGE ACCRUAL",
                  "isChargeable": false,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "UPGRADE ELIGIBILITY",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "type": "flight-offer",
      "id": "2",
      "source": "GDS",
      "instantTicketingRequired": false,
      "nonHomogeneous": false,
      "oneWay": false,
      "isUpsellOffer": false,
      "lastTicketingDate": "2025-02-17",
      "lastTicketingDateTime": "2025-02-17",
      "numberOfBookableSeats": 9,
      "itineraries": [
        {
          "duration": "PT1H20M",
          "segments": [
            {
              "departure": {
                "iataCode": "LHR",
                "terminal": "4",
                "at": "2025-02-17T11:30:00"
              },
              "arrival": {
                "iataCode": "CDG",
                "terminal": "2E",
                "at": "2025-02-17T13:50:00"
              },
              "carrierCode": "AF",
              "number": "1581",
              "aircraft": {
                "code": "223"
              },
              "operating": {
                "carrierCode": "AF"
              },
              "duration": "PT1H20M",
              "id": "2",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        },
        {
          "duration": "PT1H25M",
          "segments": [
            {
              "departure": {
                "iataCode": "CDG",
                "terminal": "2E",
                "at": "2025-08-16T13:20:00"
              },
              "arrival": {
                "iataCode": "LHR",
                "terminal": "4",
                "at": "2025-08-16T13:45:00"
              },
              "carrierCode": "AF",
              "number": "1780",
              "aircraft": {
                "code": "223"
              },
              "operating": {
                "carrierCode": "AF"
              },
              "duration": "PT1H25M",
              "id": "8",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        }
      ],
      "price": {
        "currency": "GBP",
        "total": "429.82",
        "base": "321.00",
        "fees": [
          {
            "amount": "0.00",
            "type": "SUPPLIER"
          },
          {
            "amount": "0.00",
            "type": "TICKETING"
          }
        ],
        "grandTotal": "429.82",
        "additionalServices": [
          {
            "amount": "87.60",
            "type": "CHECKED_BAGS"
          }
        ]
      },
      "pricingOptions": {
        "fareType": [
          "PUBLISHED"
        ],
        "includedCheckedBagsOnly": false
      },
      "validatingAirlineCodes": [
        "AF"
      ],
      "travelerPricings": [
        {
          "travelerId": "1",
          "fareOption": "STANDARD",
          "travelerType": "ADULT",
          "price": {
            "currency": "GBP",
            "total": "429.82",
            "base": "321.00"
          },
          "fareDetailsBySegment": [
            {
              "segmentId": "2",
              "cabin": "ECONOMY",
              "fareBasis": "TYS0AALA",
              "brandedFare": "LIGHT",
              "brandedFareLabel": "ECONOMY LIGHT",
              "class": "T",
              "includedCheckedBags": {
                "quantity": 0
              },
              "amenities": [
                {
                  "description": "CHECKED BAG 1PC OF 23KG 158CM",
                  "isChargeable": true,
                  "amenityType": "BAGGAGE",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SNACK",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "BEVERAGE",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SEAT SELECTION",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "MILEAGE ACCRUAL",
                  "isChargeable": false,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "UPGRADE ELIGIBILITY",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                }
              ]
            },
            {
              "segmentId": "8",
              "cabin": "ECONOMY",
              "fareBasis": "BYS0AALA",
              "brandedFare": "LIGHT",
              "brandedFareLabel": "ECONOMY LIGHT",
              "class": "B",
              "includedCheckedBags": {
                "quantity": 0
              },
              "amenities": [
                {
                  "description": "CHECKED BAG 1PC OF 23KG 158CM",
                  "isChargeable": true,
                  "amenityType": "BAGGAGE",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SNACK",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "BEVERAGE",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SEAT SELECTION",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "MILEAGE ACCRUAL",
                  "isChargeable": false,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "UPGRADE ELIGIBILITY",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "type": "flight-offer",
      "id": "3",
      "source": "GDS",
      "instantTicketingRequired": false,
      "nonHomogeneous": false,
      "oneWay": false,
      "isUpsellOffer": false,
      "lastTicketingDate": "2025-02-17",
      "lastTicketingDateTime": "2025-02-17",
      "numberOfBookableSeats": 9,
      "itineraries": [
        {
          "duration": "PT1H20M",
          "segments": [
            {
              "departure": {
                "iataCode": "LHR",
                "terminal": "4",
                "at": "2025-02-17T14:45:00"
              },
              "arrival": {
                "iataCode": "CDG",
                "terminal": "2E",
                "at": "2025-02-17T17:05:00"
              },
              "carrierCode": "AF",
              "number": "1781",
              "aircraft": {
                "code": "223"
              },
              "operating": {
                "carrierCode": "AF"
              },
              "duration": "PT1H20M",
              "id": "3",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        },
        {
          "duration": "PT1H25M",
          "segments": [
            {
              "departure": {
                "iataCode": "CDG",
                "terminal": "2E",
                "at": "2025-08-16T07:35:00"
              },
              "arrival": {
                "iataCode": "LHR",
                "terminal": "4",
                "at": "2025-08-16T08:00:00"
              },
              "carrierCode": "AF",
              "number": "1680",
              "aircraft": {
                "code": "223"
              },
              "operating": {
                "carrierCode": "AF"
              },
              "duration": "PT1H25M",
              "id": "7",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        }
      ],
      "price": {
        "currency": "GBP",
        "total": "429.82",
        "base": "321.00",
        "fees": [
          {
            "amount": "0.00",
            "type": "SUPPLIER"
          },
          {
            "amount": "0.00",
            "type": "TICKETING"
          }
        ],
        "grandTotal": "429.82",
        "additionalServices": [
          {
            "amount": "87.60",
            "type": "CHECKED_BAGS"
          }
        ]
      },
      "pricingOptions": {
        "fareType": [
          "PUBLISHED"
        ],
        "includedCheckedBagsOnly": false
      },
      "validatingAirlineCodes": [
        "AF"
      ],
      "travelerPricings": [
        {
          "travelerId": "1",
          "fareOption": "STANDARD",
          "travelerType": "ADULT",
          "price": {
            "currency": "GBP",
            "total": "429.82",
            "base": "321.00"
          },
          "fareDetailsBySegment": [
            {
              "segmentId": "3",
              "cabin": "ECONOMY",
              "fareBasis": "TYS0AALA",
              "brandedFare": "LIGHT",
              "brandedFareLabel": "ECONOMY LIGHT",
              "class": "T",
              "includedCheckedBags": {
                "quantity": 0
              },
              "amenities": [
                {
                  "description": "CHECKED BAG 1PC OF 23KG 158CM",
                  "isChargeable": true,
                  "amenityType": "BAGGAGE",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SNACK",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "BEVERAGE",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SEAT SELECTION",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "MILEAGE ACCRUAL",
                  "isChargeable": false,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "UPGRADE ELIGIBILITY",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                }
              ]
            },
            {
              "segmentId": "7",
              "cabin": "ECONOMY",
              "fareBasis": "BYS0AALA",
              "brandedFare": "LIGHT",
              "brandedFareLabel": "ECONOMY LIGHT",
              "class": "B",
              "includedCheckedBags": {
                "quantity": 0
              },
              "amenities": [
                {
                  "description": "CHECKED BAG 1PC OF 23KG 158CM",
                  "isChargeable": true,
                  "amenityType": "BAGGAGE",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SNACK",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "BEVERAGE",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SEAT SELECTION",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "MILEAGE ACCRUAL",
                  "isChargeable": false,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "UPGRADE ELIGIBILITY",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "type": "flight-offer",
      "id": "4",
      "source": "GDS",
      "instantTicketingRequired": false,
      "nonHomogeneous": false,
      "oneWay": false,
      "isUpsellOffer": false,
      "lastTicketingDate": "2025-02-17",
      "lastTicketingDateTime": "2025-02-17",
      "numberOfBookableSeats": 9,
      "itineraries": [
        {
          "duration": "PT1H20M",
          "segments": [
            {
              "departure": {
                "iataCode": "LHR",
                "terminal": "4",
                "at": "2025-02-17T14:45:00"
              },
              "arrival": {
                "iataCode": "CDG",
                "terminal": "2E",
                "at": "2025-02-17T17:05:00"
              },
              "carrierCode": "AF",
              "number": "1781",
              "aircraft": {
                "code": "223"
              },
              "operating": {
                "carrierCode": "AF"
              },
              "duration": "PT1H20M",
              "id": "3",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        },
        {
          "duration": "PT1H25M",
          "segments": [
            {
              "departure": {
                "iataCode": "CDG",
                "terminal": "2E",
                "at": "2025-08-16T13:20:00"
              },
              "arrival": {
                "iataCode": "LHR",
                "terminal": "4",
                "at": "2025-08-16T13:45:00"
              },
              "carrierCode": "AF",
              "number": "1780",
              "aircraft": {
                "code": "223"
              },
              "operating": {
                "carrierCode": "AF"
              },
              "duration": "PT1H25M",
              "id": "8",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        }
      ],
      "price": {
        "currency": "GBP",
        "total": "429.82",
        "base": "321.00",
        "fees": [
          {
            "amount": "0.00",
            "type": "SUPPLIER"
          },
          {
            "amount": "0.00",
            "type": "TICKETING"
          }
        ],
        "grandTotal": "429.82",
        "additionalServices": [
          {
            "amount": "87.60",
            "type": "CHECKED_BAGS"
          }
        ]
      },
      "pricingOptions": {
        "fareType": [
          "PUBLISHED"
        ],
        "includedCheckedBagsOnly": false
      },
      "validatingAirlineCodes": [
        "AF"
      ],
      "travelerPricings": [
        {
          "travelerId": "1",
          "fareOption": "STANDARD",
          "travelerType": "ADULT",
          "price": {
            "currency": "GBP",
            "total": "429.82",
            "base": "321.00"
          },
          "fareDetailsBySegment": [
            {
              "segmentId": "3",
              "cabin": "ECONOMY",
              "fareBasis": "TYS0AALA",
              "brandedFare": "LIGHT",
              "brandedFareLabel": "ECONOMY LIGHT",
              "class": "T",
              "includedCheckedBags": {
                "quantity": 0
              },
              "amenities": [
                {
                  "description": "CHECKED BAG 1PC OF 23KG 158CM",
                  "isChargeable": true,
                  "amenityType": "BAGGAGE",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SNACK",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "BEVERAGE",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SEAT SELECTION",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "MILEAGE ACCRUAL",
                  "isChargeable": false,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "UPGRADE ELIGIBILITY",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                }
              ]
            },
            {
              "segmentId": "8",
              "cabin": "ECONOMY",
              "fareBasis": "BYS0AALA",
              "brandedFare": "LIGHT",
              "brandedFareLabel": "ECONOMY LIGHT",
              "class": "B",
              "includedCheckedBags": {
                "quantity": 0
              },
              "amenities": [
                {
                  "description": "CHECKED BAG 1PC OF 23KG 158CM",
                  "isChargeable": true,
                  "amenityType": "BAGGAGE",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SNACK",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "BEVERAGE",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SEAT SELECTION",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "MILEAGE ACCRUAL",
                  "isChargeable": false,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "UPGRADE ELIGIBILITY",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "type": "flight-offer",
      "id": "5",
      "source": "GDS",
      "instantTicketingRequired": false,
      "nonHomogeneous": false,
      "oneWay": false,
      "isUpsellOffer": false,
      "lastTicketingDate": "2025-02-17",
      "lastTicketingDateTime": "2025-02-17",
      "numberOfBookableSeats": 9,
      "itineraries": [
        {
          "duration": "PT1H20M",
          "segments": [
            {
              "departure": {
                "iataCode": "LHR",
                "terminal": "4",
                "at": "2025-02-17T17:35:00"
              },
              "arrival": {
                "iataCode": "CDG",
                "terminal": "2E",
                "at": "2025-02-17T19:55:00"
              },
              "carrierCode": "AF",
              "number": "1281",
              "aircraft": {
                "code": "223"
              },
              "operating": {
                "carrierCode": "AF"
              },
              "duration": "PT1H20M",
              "id": "4",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        },
        {
          "duration": "PT1H25M",
          "segments": [
            {
              "departure": {
                "iataCode": "CDG",
                "terminal": "2E",
                "at": "2025-08-16T07:35:00"
              },
              "arrival": {
                "iataCode": "LHR",
                "terminal": "4",
                "at": "2025-08-16T08:00:00"
              },
              "carrierCode": "AF",
              "number": "1680",
              "aircraft": {
                "code": "223"
              },
              "operating": {
                "carrierCode": "AF"
              },
              "duration": "PT1H25M",
              "id": "7",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        }
      ],
      "price": {
        "currency": "GBP",
        "total": "429.82",
        "base": "321.00",
        "fees": [
          {
            "amount": "0.00",
            "type": "SUPPLIER"
          },
          {
            "amount": "0.00",
            "type": "TICKETING"
          }
        ],
        "grandTotal": "429.82",
        "additionalServices": [
          {
            "amount": "87.60",
            "type": "CHECKED_BAGS"
          }
        ]
      },
      "pricingOptions": {
        "fareType": [
          "PUBLISHED"
        ],
        "includedCheckedBagsOnly": false
      },
      "validatingAirlineCodes": [
        "AF"
      ],
      "travelerPricings": [
        {
          "travelerId": "1",
          "fareOption": "STANDARD",
          "travelerType": "ADULT",
          "price": {
            "currency": "GBP",
            "total": "429.82",
            "base": "321.00"
          },
          "fareDetailsBySegment": [
            {
              "segmentId": "4",
              "cabin": "ECONOMY",
              "fareBasis": "TYS0AALA",
              "brandedFare": "LIGHT",
              "brandedFareLabel": "ECONOMY LIGHT",
              "class": "T",
              "includedCheckedBags": {
                "quantity": 0
              },
              "amenities": [
                {
                  "description": "CHECKED BAG 1PC OF 23KG 158CM",
                  "isChargeable": true,
                  "amenityType": "BAGGAGE",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SNACK",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "BEVERAGE",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SEAT SELECTION",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "MILEAGE ACCRUAL",
                  "isChargeable": false,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "UPGRADE ELIGIBILITY",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                }
              ]
            },
            {
              "segmentId": "7",
              "cabin": "ECONOMY",
              "fareBasis": "BYS0AALA",
              "brandedFare": "LIGHT",
              "brandedFareLabel": "ECONOMY LIGHT",
              "class": "B",
              "includedCheckedBags": {
                "quantity": 0
              },
              "amenities": [
                {
                  "description": "CHECKED BAG 1PC OF 23KG 158CM",
                  "isChargeable": true,
                  "amenityType": "BAGGAGE",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SNACK",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "BEVERAGE",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SEAT SELECTION",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "MILEAGE ACCRUAL",
                  "isChargeable": false,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "UPGRADE ELIGIBILITY",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "type": "flight-offer",
      "id": "6",
      "source": "GDS",
      "instantTicketingRequired": false,
      "nonHomogeneous": false,
      "oneWay": false,
      "isUpsellOffer": false,
      "lastTicketingDate": "2025-02-17",
      "lastTicketingDateTime": "2025-02-17",
      "numberOfBookableSeats": 9,
      "itineraries": [
        {
          "duration": "PT1H20M",
          "segments": [
            {
              "departure": {
                "iataCode": "LHR",
                "terminal": "4",
                "at": "2025-02-17T17:35:00"
              },
              "arrival": {
                "iataCode": "CDG",
                "terminal": "2E",
                "at": "2025-02-17T19:55:00"
              },
              "carrierCode": "AF",
              "number": "1281",
              "aircraft": {
                "code": "223"
              },
              "operating": {
                "carrierCode": "AF"
              },
              "duration": "PT1H20M",
              "id": "4",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        },
        {
          "duration": "PT1H25M",
          "segments": [
            {
              "departure": {
                "iataCode": "CDG",
                "terminal": "2E",
                "at": "2025-08-16T13:20:00"
              },
              "arrival": {
                "iataCode": "LHR",
                "terminal": "4",
                "at": "2025-08-16T13:45:00"
              },
              "carrierCode": "AF",
              "number": "1780",
              "aircraft": {
                "code": "223"
              },
              "operating": {
                "carrierCode": "AF"
              },
              "duration": "PT1H25M",
              "id": "8",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        }
      ],
      "price": {
        "currency": "GBP",
        "total": "429.82",
        "base": "321.00",
        "fees": [
          {
            "amount": "0.00",
            "type": "SUPPLIER"
          },
          {
            "amount": "0.00",
            "type": "TICKETING"
          }
        ],
        "grandTotal": "429.82",
        "additionalServices": [
          {
            "amount": "87.60",
            "type": "CHECKED_BAGS"
          }
        ]
      },
      "pricingOptions": {
        "fareType": [
          "PUBLISHED"
        ],
        "includedCheckedBagsOnly": false
      },
      "validatingAirlineCodes": [
        "AF"
      ],
      "travelerPricings": [
        {
          "travelerId": "1",
          "fareOption": "STANDARD",
          "travelerType": "ADULT",
          "price": {
            "currency": "GBP",
            "total": "429.82",
            "base": "321.00"
          },
          "fareDetailsBySegment": [
            {
              "segmentId": "4",
              "cabin": "ECONOMY",
              "fareBasis": "TYS0AALA",
              "brandedFare": "LIGHT",
              "brandedFareLabel": "ECONOMY LIGHT",
              "class": "T",
              "includedCheckedBags": {
                "quantity": 0
              },
              "amenities": [
                {
                  "description": "CHECKED BAG 1PC OF 23KG 158CM",
                  "isChargeable": true,
                  "amenityType": "BAGGAGE",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SNACK",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "BEVERAGE",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SEAT SELECTION",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "MILEAGE ACCRUAL",
                  "isChargeable": false,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "UPGRADE ELIGIBILITY",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                }
              ]
            },
            {
              "segmentId": "8",
              "cabin": "ECONOMY",
              "fareBasis": "BYS0AALA",
              "brandedFare": "LIGHT",
              "brandedFareLabel": "ECONOMY LIGHT",
              "class": "B",
              "includedCheckedBags": {
                "quantity": 0
              },
              "amenities": [
                {
                  "description": "CHECKED BAG 1PC OF 23KG 158CM",
                  "isChargeable": true,
                  "amenityType": "BAGGAGE",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SNACK",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "BEVERAGE",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SEAT SELECTION",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "MILEAGE ACCRUAL",
                  "isChargeable": false,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "UPGRADE ELIGIBILITY",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "type": "flight-offer",
      "id": "7",
      "source": "GDS",
      "instantTicketingRequired": false,
      "nonHomogeneous": false,
      "oneWay": false,
      "isUpsellOffer": false,
      "lastTicketingDate": "2025-02-17",
      "lastTicketingDateTime": "2025-02-17",
      "numberOfBookableSeats": 9,
      "itineraries": [
        {
          "duration": "PT1H20M",
          "segments": [
            {
              "departure": {
                "iataCode": "LHR",
                "terminal": "4",
                "at": "2025-02-17T19:35:00"
              },
              "arrival": {
                "iataCode": "CDG",
                "terminal": "2E",
                "at": "2025-02-17T21:55:00"
              },
              "carrierCode": "AF",
              "number": "1181",
              "aircraft": {
                "code": "223"
              },
              "operating": {
                "carrierCode": "AF"
              },
              "duration": "PT1H20M",
              "id": "5",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        },
        {
          "duration": "PT1H25M",
          "segments": [
            {
              "departure": {
                "iataCode": "CDG",
                "terminal": "2E",
                "at": "2025-08-16T07:35:00"
              },
              "arrival": {
                "iataCode": "LHR",
                "terminal": "4",
                "at": "2025-08-16T08:00:00"
              },
              "carrierCode": "AF",
              "number": "1680",
              "aircraft": {
                "code": "223"
              },
              "operating": {
                "carrierCode": "AF"
              },
              "duration": "PT1H25M",
              "id": "7",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        }
      ],
      "price": {
        "currency": "GBP",
        "total": "429.82",
        "base": "321.00",
        "fees": [
          {
            "amount": "0.00",
            "type": "SUPPLIER"
          },
          {
            "amount": "0.00",
            "type": "TICKETING"
          }
        ],
        "grandTotal": "429.82",
        "additionalServices": [
          {
            "amount": "87.60",
            "type": "CHECKED_BAGS"
          }
        ]
      },
      "pricingOptions": {
        "fareType": [
          "PUBLISHED"
        ],
        "includedCheckedBagsOnly": false
      },
      "validatingAirlineCodes": [
        "AF"
      ],
      "travelerPricings": [
        {
          "travelerId": "1",
          "fareOption": "STANDARD",
          "travelerType": "ADULT",
          "price": {
            "currency": "GBP",
            "total": "429.82",
            "base": "321.00"
          },
          "fareDetailsBySegment": [
            {
              "segmentId": "5",
              "cabin": "ECONOMY",
              "fareBasis": "TYS0AALA",
              "brandedFare": "LIGHT",
              "brandedFareLabel": "ECONOMY LIGHT",
              "class": "T",
              "includedCheckedBags": {
                "quantity": 0
              },
              "amenities": [
                {
                  "description": "CHECKED BAG 1PC OF 23KG 158CM",
                  "isChargeable": true,
                  "amenityType": "BAGGAGE",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SNACK",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "BEVERAGE",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SEAT SELECTION",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "MILEAGE ACCRUAL",
                  "isChargeable": false,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "UPGRADE ELIGIBILITY",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                }
              ]
            },
            {
              "segmentId": "7",
              "cabin": "ECONOMY",
              "fareBasis": "BYS0AALA",
              "brandedFare": "LIGHT",
              "brandedFareLabel": "ECONOMY LIGHT",
              "class": "B",
              "includedCheckedBags": {
                "quantity": 0
              },
              "amenities": [
                {
                  "description": "CHECKED BAG 1PC OF 23KG 158CM",
                  "isChargeable": true,
                  "amenityType": "BAGGAGE",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SNACK",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "BEVERAGE",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SEAT SELECTION",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "MILEAGE ACCRUAL",
                  "isChargeable": false,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "UPGRADE ELIGIBILITY",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "type": "flight-offer",
      "id": "8",
      "source": "GDS",
      "instantTicketingRequired": false,
      "nonHomogeneous": false,
      "oneWay": false,
      "isUpsellOffer": false,
      "lastTicketingDate": "2025-02-17",
      "lastTicketingDateTime": "2025-02-17",
      "numberOfBookableSeats": 9,
      "itineraries": [
        {
          "duration": "PT1H20M",
          "segments": [
            {
              "departure": {
                "iataCode": "LHR",
                "terminal": "4",
                "at": "2025-02-17T19:35:00"
              },
              "arrival": {
                "iataCode": "CDG",
                "terminal": "2E",
                "at": "2025-02-17T21:55:00"
              },
              "carrierCode": "AF",
              "number": "1181",
              "aircraft": {
                "code": "223"
              },
              "operating": {
                "carrierCode": "AF"
              },
              "duration": "PT1H20M",
              "id": "5",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        },
        {
          "duration": "PT1H25M",
          "segments": [
            {
              "departure": {
                "iataCode": "CDG",
                "terminal": "2E",
                "at": "2025-08-16T13:20:00"
              },
              "arrival": {
                "iataCode": "LHR",
                "terminal": "4",
                "at": "2025-08-16T13:45:00"
              },
              "carrierCode": "AF",
              "number": "1780",
              "aircraft": {
                "code": "223"
              },
              "operating": {
                "carrierCode": "AF"
              },
              "duration": "PT1H25M",
              "id": "8",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        }
      ],
      "price": {
        "currency": "GBP",
        "total": "429.82",
        "base": "321.00",
        "fees": [
          {
            "amount": "0.00",
            "type": "SUPPLIER"
          },
          {
            "amount": "0.00",
            "type": "TICKETING"
          }
        ],
        "grandTotal": "429.82",
        "additionalServices": [
          {
            "amount": "87.60",
            "type": "CHECKED_BAGS"
          }
        ]
      },
      "pricingOptions": {
        "fareType": [
          "PUBLISHED"
        ],
        "includedCheckedBagsOnly": false
      },
      "validatingAirlineCodes": [
        "AF"
      ],
      "travelerPricings": [
        {
          "travelerId": "1",
          "fareOption": "STANDARD",
          "travelerType": "ADULT",
          "price": {
            "currency": "GBP",
            "total": "429.82",
            "base": "321.00"
          },
          "fareDetailsBySegment": [
            {
              "segmentId": "5",
              "cabin": "ECONOMY",
              "fareBasis": "TYS0AALA",
              "brandedFare": "LIGHT",
              "brandedFareLabel": "ECONOMY LIGHT",
              "class": "T",
              "includedCheckedBags": {
                "quantity": 0
              },
              "amenities": [
                {
                  "description": "CHECKED BAG 1PC OF 23KG 158CM",
                  "isChargeable": true,
                  "amenityType": "BAGGAGE",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SNACK",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "BEVERAGE",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SEAT SELECTION",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "MILEAGE ACCRUAL",
                  "isChargeable": false,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "UPGRADE ELIGIBILITY",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                }
              ]
            },
            {
              "segmentId": "8",
              "cabin": "ECONOMY",
              "fareBasis": "BYS0AALA",
              "brandedFare": "LIGHT",
              "brandedFareLabel": "ECONOMY LIGHT",
              "class": "B",
              "includedCheckedBags": {
                "quantity": 0
              },
              "amenities": [
                {
                  "description": "CHECKED BAG 1PC OF 23KG 158CM",
                  "isChargeable": true,
                  "amenityType": "BAGGAGE",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SNACK",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "BEVERAGE",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SEAT SELECTION",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "MILEAGE ACCRUAL",
                  "isChargeable": false,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "UPGRADE ELIGIBILITY",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "type": "flight-offer",
      "id": "9",
      "source": "GDS",
      "instantTicketingRequired": false,
      "nonHomogeneous": false,
      "oneWay": false,
      "isUpsellOffer": false,
      "lastTicketingDate": "2025-02-17",
      "lastTicketingDateTime": "2025-02-17",
      "numberOfBookableSeats": 9,
      "itineraries": [
        {
          "duration": "PT1H25M",
          "segments": [
            {
              "departure": {
                "iataCode": "LHR",
                "terminal": "4",
                "at": "2025-02-17T09:00:00"
              },
              "arrival": {
                "iataCode": "CDG",
                "terminal": "2E",
                "at": "2025-02-17T11:25:00"
              },
              "carrierCode": "AF",
              "number": "1681",
              "aircraft": {
                "code": "223"
              },
              "operating": {
                "carrierCode": "AF"
              },
              "duration": "PT1H25M",
              "id": "6",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        },
        {
          "duration": "PT1H25M",
          "segments": [
            {
              "departure": {
                "iataCode": "CDG",
                "terminal": "2E",
                "at": "2025-08-16T07:35:00"
              },
              "arrival": {
                "iataCode": "LHR",
                "terminal": "4",
                "at": "2025-08-16T08:00:00"
              },
              "carrierCode": "AF",
              "number": "1680",
              "aircraft": {
                "code": "223"
              },
              "operating": {
                "carrierCode": "AF"
              },
              "duration": "PT1H25M",
              "id": "7",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        }
      ],
      "price": {
        "currency": "GBP",
        "total": "429.82",
        "base": "321.00",
        "fees": [
          {
            "amount": "0.00",
            "type": "SUPPLIER"
          },
          {
            "amount": "0.00",
            "type": "TICKETING"
          }
        ],
        "grandTotal": "429.82",
        "additionalServices": [
          {
            "amount": "87.60",
            "type": "CHECKED_BAGS"
          }
        ]
      },
      "pricingOptions": {
        "fareType": [
          "PUBLISHED"
        ],
        "includedCheckedBagsOnly": false
      },
      "validatingAirlineCodes": [
        "AF"
      ],
      "travelerPricings": [
        {
          "travelerId": "1",
          "fareOption": "STANDARD",
          "travelerType": "ADULT",
          "price": {
            "currency": "GBP",
            "total": "429.82",
            "base": "321.00"
          },
          "fareDetailsBySegment": [
            {
              "segmentId": "6",
              "cabin": "ECONOMY",
              "fareBasis": "TYS0AALA",
              "brandedFare": "LIGHT",
              "brandedFareLabel": "ECONOMY LIGHT",
              "class": "T",
              "includedCheckedBags": {
                "quantity": 0
              },
              "amenities": [
                {
                  "description": "CHECKED BAG 1PC OF 23KG 158CM",
                  "isChargeable": true,
                  "amenityType": "BAGGAGE",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SNACK",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "BEVERAGE",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SEAT SELECTION",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "MILEAGE ACCRUAL",
                  "isChargeable": false,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "UPGRADE ELIGIBILITY",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                }
              ]
            },
            {
              "segmentId": "7",
              "cabin": "ECONOMY",
              "fareBasis": "BYS0AALA",
              "brandedFare": "LIGHT",
              "brandedFareLabel": "ECONOMY LIGHT",
              "class": "B",
              "includedCheckedBags": {
                "quantity": 0
              },
              "amenities": [
                {
                  "description": "CHECKED BAG 1PC OF 23KG 158CM",
                  "isChargeable": true,
                  "amenityType": "BAGGAGE",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SNACK",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "BEVERAGE",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SEAT SELECTION",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "MILEAGE ACCRUAL",
                  "isChargeable": false,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "UPGRADE ELIGIBILITY",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "type": "flight-offer",
      "id": "10",
      "source": "GDS",
      "instantTicketingRequired": false,
      "nonHomogeneous": false,
      "oneWay": false,
      "isUpsellOffer": false,
      "lastTicketingDate": "2025-02-17",
      "lastTicketingDateTime": "2025-02-17",
      "numberOfBookableSeats": 9,
      "itineraries": [
        {
          "duration": "PT1H25M",
          "segments": [
            {
              "departure": {
                "iataCode": "LHR",
                "terminal": "4",
                "at": "2025-02-17T09:00:00"
              },
              "arrival": {
                "iataCode": "CDG",
                "terminal": "2E",
                "at": "2025-02-17T11:25:00"
              },
              "carrierCode": "AF",
              "number": "1681",
              "aircraft": {
                "code": "223"
              },
              "operating": {
                "carrierCode": "AF"
              },
              "duration": "PT1H25M",
              "id": "6",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        },
        {
          "duration": "PT1H25M",
          "segments": [
            {
              "departure": {
                "iataCode": "CDG",
                "terminal": "2E",
                "at": "2025-08-16T13:20:00"
              },
              "arrival": {
                "iataCode": "LHR",
                "terminal": "4",
                "at": "2025-08-16T13:45:00"
              },
              "carrierCode": "AF",
              "number": "1780",
              "aircraft": {
                "code": "223"
              },
              "operating": {
                "carrierCode": "AF"
              },
              "duration": "PT1H25M",
              "id": "8",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        }
      ],
      "price": {
        "currency": "GBP",
        "total": "429.82",
        "base": "321.00",
        "fees": [
          {
            "amount": "0.00",
            "type": "SUPPLIER"
          },
          {
            "amount": "0.00",
            "type": "TICKETING"
          }
        ],
        "grandTotal": "429.82",
        "additionalServices": [
          {
            "amount": "87.60",
            "type": "CHECKED_BAGS"
          }
        ]
      },
      "pricingOptions": {
        "fareType": [
          "PUBLISHED"
        ],
        "includedCheckedBagsOnly": false
      },
      "validatingAirlineCodes": [
        "AF"
      ],
      "travelerPricings": [
        {
          "travelerId": "1",
          "fareOption": "STANDARD",
          "travelerType": "ADULT",
          "price": {
            "currency": "GBP",
            "total": "429.82",
            "base": "321.00"
          },
          "fareDetailsBySegment": [
            {
              "segmentId": "6",
              "cabin": "ECONOMY",
              "fareBasis": "TYS0AALA",
              "brandedFare": "LIGHT",
              "brandedFareLabel": "ECONOMY LIGHT",
              "class": "T",
              "includedCheckedBags": {
                "quantity": 0
              },
              "amenities": [
                {
                  "description": "CHECKED BAG 1PC OF 23KG 158CM",
                  "isChargeable": true,
                  "amenityType": "BAGGAGE",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SNACK",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "BEVERAGE",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SEAT SELECTION",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "MILEAGE ACCRUAL",
                  "isChargeable": false,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "UPGRADE ELIGIBILITY",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                }
              ]
            },
            {
              "segmentId": "8",
              "cabin": "ECONOMY",
              "fareBasis": "BYS0AALA",
              "brandedFare": "LIGHT",
              "brandedFareLabel": "ECONOMY LIGHT",
              "class": "B",
              "includedCheckedBags": {
                "quantity": 0
              },
              "amenities": [
                {
                  "description": "CHECKED BAG 1PC OF 23KG 158CM",
                  "isChargeable": true,
                  "amenityType": "BAGGAGE",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SNACK",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "BEVERAGE",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SEAT SELECTION",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "MILEAGE ACCRUAL",
                  "isChargeable": false,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "UPGRADE ELIGIBILITY",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "type": "flight-offer",
      "id": "11",
      "source": "GDS",
      "instantTicketingRequired": false,
      "nonHomogeneous": false,
      "oneWay": false,
      "isUpsellOffer": false,
      "lastTicketingDate": "2025-02-17",
      "lastTicketingDateTime": "2025-02-17",
      "numberOfBookableSeats": 8,
      "itineraries": [
        {
          "duration": "PT1H20M",
          "segments": [
            {
              "departure": {
                "iataCode": "LHR",
                "terminal": "4",
                "at": "2025-02-17T06:20:00"
              },
              "arrival": {
                "iataCode": "CDG",
                "terminal": "2E",
                "at": "2025-02-17T08:40:00"
              },
              "carrierCode": "AF",
              "number": "1381",
              "aircraft": {
                "code": "223"
              },
              "operating": {
                "carrierCode": "AF"
              },
              "duration": "PT1H20M",
              "id": "1",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        },
        {
          "duration": "PT1H25M",
          "segments": [
            {
              "departure": {
                "iataCode": "CDG",
                "terminal": "2E",
                "at": "2025-08-16T07:35:00"
              },
              "arrival": {
                "iataCode": "LHR",
                "terminal": "4",
                "at": "2025-08-16T08:00:00"
              },
              "carrierCode": "AF",
              "number": "1680",
              "aircraft": {
                "code": "223"
              },
              "operating": {
                "carrierCode": "AF"
              },
              "duration": "PT1H25M",
              "id": "7",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        }
      ],
      "price": {
        "currency": "GBP",
        "total": "449.82",
        "base": "341.00",
        "fees": [
          {
            "amount": "0.00",
            "type": "SUPPLIER"
          },
          {
            "amount": "0.00",
            "type": "TICKETING"
          }
        ],
        "grandTotal": "449.82",
        "additionalServices": [
          {
            "amount": "87.60",
            "type": "CHECKED_BAGS"
          }
        ]
      },
      "pricingOptions": {
        "fareType": [
          "PUBLISHED"
        ],
        "includedCheckedBagsOnly": false
      },
      "validatingAirlineCodes": [
        "AF"
      ],
      "travelerPricings": [
        {
          "travelerId": "1",
          "fareOption": "STANDARD",
          "travelerType": "ADULT",
          "price": {
            "currency": "GBP",
            "total": "449.82",
            "base": "341.00"
          },
          "fareDetailsBySegment": [
            {
              "segmentId": "1",
              "cabin": "ECONOMY",
              "fareBasis": "LYS0AALA",
              "brandedFare": "LIGHT",
              "brandedFareLabel": "ECONOMY LIGHT",
              "class": "L",
              "includedCheckedBags": {
                "quantity": 0
              },
              "amenities": [
                {
                  "description": "CHECKED BAG 1PC OF 23KG 158CM",
                  "isChargeable": true,
                  "amenityType": "BAGGAGE",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SNACK",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "BEVERAGE",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SEAT SELECTION",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "MILEAGE ACCRUAL",
                  "isChargeable": false,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "UPGRADE ELIGIBILITY",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                }
              ]
            },
            {
              "segmentId": "7",
              "cabin": "ECONOMY",
              "fareBasis": "BYS0AALA",
              "brandedFare": "LIGHT",
              "brandedFareLabel": "ECONOMY LIGHT",
              "class": "B",
              "includedCheckedBags": {
                "quantity": 0
              },
              "amenities": [
                {
                  "description": "CHECKED BAG 1PC OF 23KG 158CM",
                  "isChargeable": true,
                  "amenityType": "BAGGAGE",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SNACK",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "BEVERAGE",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SEAT SELECTION",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "MILEAGE ACCRUAL",
                  "isChargeable": false,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "UPGRADE ELIGIBILITY",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "type": "flight-offer",
      "id": "12",
      "source": "GDS",
      "instantTicketingRequired": false,
      "nonHomogeneous": false,
      "oneWay": false,
      "isUpsellOffer": false,
      "lastTicketingDate": "2025-02-17",
      "lastTicketingDateTime": "2025-02-17",
      "numberOfBookableSeats": 8,
      "itineraries": [
        {
          "duration": "PT1H20M",
          "segments": [
            {
              "departure": {
                "iataCode": "LHR",
                "terminal": "4",
                "at": "2025-02-17T06:20:00"
              },
              "arrival": {
                "iataCode": "CDG",
                "terminal": "2E",
                "at": "2025-02-17T08:40:00"
              },
              "carrierCode": "AF",
              "number": "1381",
              "aircraft": {
                "code": "223"
              },
              "operating": {
                "carrierCode": "AF"
              },
              "duration": "PT1H20M",
              "id": "1",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        },
        {
          "duration": "PT1H25M",
          "segments": [
            {
              "departure": {
                "iataCode": "CDG",
                "terminal": "2E",
                "at": "2025-08-16T13:20:00"
              },
              "arrival": {
                "iataCode": "LHR",
                "terminal": "4",
                "at": "2025-08-16T13:45:00"
              },
              "carrierCode": "AF",
              "number": "1780",
              "aircraft": {
                "code": "223"
              },
              "operating": {
                "carrierCode": "AF"
              },
              "duration": "PT1H25M",
              "id": "8",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        }
      ],
      "price": {
        "currency": "GBP",
        "total": "449.82",
        "base": "341.00",
        "fees": [
          {
            "amount": "0.00",
            "type": "SUPPLIER"
          },
          {
            "amount": "0.00",
            "type": "TICKETING"
          }
        ],
        "grandTotal": "449.82",
        "additionalServices": [
          {
            "amount": "87.60",
            "type": "CHECKED_BAGS"
          }
        ]
      },
      "pricingOptions": {
        "fareType": [
          "PUBLISHED"
        ],
        "includedCheckedBagsOnly": false
      },
      "validatingAirlineCodes": [
        "AF"
      ],
      "travelerPricings": [
        {
          "travelerId": "1",
          "fareOption": "STANDARD",
          "travelerType": "ADULT",
          "price": {
            "currency": "GBP",
            "total": "449.82",
            "base": "341.00"
          },
          "fareDetailsBySegment": [
            {
              "segmentId": "1",
              "cabin": "ECONOMY",
              "fareBasis": "LYS0AALA",
              "brandedFare": "LIGHT",
              "brandedFareLabel": "ECONOMY LIGHT",
              "class": "L",
              "includedCheckedBags": {
                "quantity": 0
              },
              "amenities": [
                {
                  "description": "CHECKED BAG 1PC OF 23KG 158CM",
                  "isChargeable": true,
                  "amenityType": "BAGGAGE",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SNACK",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "BEVERAGE",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SEAT SELECTION",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "MILEAGE ACCRUAL",
                  "isChargeable": false,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "UPGRADE ELIGIBILITY",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                }
              ]
            },
            {
              "segmentId": "8",
              "cabin": "ECONOMY",
              "fareBasis": "BYS0AALA",
              "brandedFare": "LIGHT",
              "brandedFareLabel": "ECONOMY LIGHT",
              "class": "B",
              "includedCheckedBags": {
                "quantity": 0
              },
              "amenities": [
                {
                  "description": "CHECKED BAG 1PC OF 23KG 158CM",
                  "isChargeable": true,
                  "amenityType": "BAGGAGE",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SNACK",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "BEVERAGE",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "SEAT SELECTION",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "MILEAGE ACCRUAL",
                  "isChargeable": false,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                },
                {
                  "description": "UPGRADE ELIGIBILITY",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": {
                    "name": "BrandedFare"
                  }
                }
              ]
            }
          ]
        }
      ]
    }
  ],
  "dictionaries": {
    "locations": {
      "CDG": {
        "cityCode": "PAR",
        "countryCode": "FR"
      },
      "LHR": {
        "cityCode": "LON",
        "countryCode": "GB"
      }
    },
    "aircraft": {
      "223": "AIRBUS  A220-300"
    },
    "currencies": {
      "GBP": "POUND STERLING"
    },
    "carriers": {
      "AF": "AIR FRANCE"
    }
  }
}'''
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
#
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = fs.get_destination_code(row["city"])
print(f"sheet data:\n {sheet_data}")

dm.destination_data = sheet_data
#pprint(sheet_data)
dm.update_destination_codes()
#fs.get_destination_code("LONDON")

tomorrow = datetime.now() + timedelta(days=1)
print(tomorrow)

return_date = tomorrow + timedelta(days=(6*30))
print(return_date)
for destination in sheet_data:
    print(f"City: {destination["city"]}...")
    flights = fs.check_flights(ORIGIN_CITY, destination["iataCode"], from_date=tomorrow, to_date=return_date)
    pprint(flights)
    time.sleep(5)
#new_data["data"][0]["price"]["total"]

for flight in flights:
    price = flight["price"]["total"]
    print(f"{price:}")
    departure_airport = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    print(f"{departure_airport:}")
    arrival_airport = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    print(f"{arrival_airport:}")
    carrier = flight["itineraries"][0]["segments"][0]["carrierCode"]
    print(f"{carrier:}")


