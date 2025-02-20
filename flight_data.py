class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price, departure_airport, arrival_airport, carrier, from_date, return_date):
        self.price = price
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.carrier = carrier
        self.from_date = from_date
        self.return_date = return_date


def find_cheapest_flight(data):
    if data is None or not data["data"]:
        print("No data available")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")

    first_flight = data["data"][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    departure_airport = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    arrival_airport = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

    cheapest_flight = FlightData(lowest_price, departure_airport, arrival_airport, out_date, return_date)

    for flight in data["data"]:
        price = float(first_flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price
            departure_airport = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            arrival_airport = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            cheapest_flight = FlightData(lowest_price, departure_airport, arrival_airport, out_date, return_date)

    return cheapest_flight
