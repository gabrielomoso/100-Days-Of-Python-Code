import requests
from pprint import pprint

KEY = "gLM3r-7nedGXpn58tt2BTqH28nEJMpXk"
ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
HEADER = {
    "apikey": KEY
}


class FlightSearch:
    """This class talks with the location part of the tequila.kiwi API"""

    def get_iataCode(self, city):
        """This method returns the iataCode of a city"""

        parameters = {
            "term": city,
            "location_types": "airport",
            "limit": "1"


        }
        response = requests.get(url=ENDPOINT, params=parameters, headers=HEADER)
        response.raise_for_status()
        return response.json()["locations"][0]["city"]["code"]
