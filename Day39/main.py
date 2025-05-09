# Class imports
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

# Class initializations
data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()
notification = NotificationManager()

# Getting the values in the google sheet
sheety_data = data_manager.getdata()

for item in sheety_data:

    # Updating the city iataCode if empty
    if item["iataCode"] == "":
        item["iataCode"] = flight_search.get_iataCode(item["city"])
        new_data = {
            "id": item["id"],
            "iataCode": item["iataCode"]
        }
        data_manager.update_iataCode(new_data)

    # This gets the lowest flight data
    flight = flight_data.search_flights(item["iataCode"])

    # This sends a message once we get a low budget price
    if flight["price"] < item["lowestPrice"]:
        notification.send_notification(flight)
    else:
        print(f"No match for {item['city']}")
