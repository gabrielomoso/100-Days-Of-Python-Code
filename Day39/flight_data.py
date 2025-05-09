from datetime import datetime
from dateutil.relativedelta import relativedelta
import requests

KEY = ""
ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
HEADER = {
    "apikey": KEY
}
FLY_FROM = "LOS"
# Get today's date
current_date = datetime.now()

# Calculate the date 6 months from today
six_months_later = current_date + relativedelta(months=+6)


class FlightData:
    """This class talks with the Search part of the tequila.kiwi API"""

    def search_flights(self, iataCode):
        """This method searches for flights and sends back the cheapest for a particular destination"""

        data = {"price": ""}
        parameters = {
            "fly_from": FLY_FROM,
            "fly_to": iataCode,
            "date_from": current_date.strftime("%Y-%m-%d"),
            "date_to": six_months_later.strftime("%Y-%m-%d"),
            "nights_in_dst_from": "7",
            "nights_in_dst_to": "28",
            "curr": "NGN"
        }

        response = requests.get(url=ENDPOINT, params=parameters, headers=HEADER)
        response.raise_for_status()
        for item in response.json()["data"]:
            if data["price"] == "":
                data = item
            elif item["price"] < data["price"]:
                data = item

        return data