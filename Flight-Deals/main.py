#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import Sheety_Manager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
import time
from notification_manager import NotificationManager


notification_manager = NotificationManager()

sheety_data = Sheety_Manager()

sheet_data = sheety_data.get_destination_data()


flight_search = FlightSearch()

ORIGIN_CITY_IATA = "ICN"

tomorrow = datetime.today() + timedelta(days=1)
six_months_from_today = datetime.today() + timedelta(days=180)

for destination in sheet_data:
    print(f"Getting flights for: {destination["city"]}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )

    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price}")
    # Slowing down requests to avoid rate limit
    time.sleep(2)

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")
        notification_manager.send_sms(
            message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
                         f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                         f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )


