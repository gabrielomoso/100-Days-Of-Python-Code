import requests

TOKEN = ""
ENDPOINT = "https://api.sheety.co/60e4509708e197940c7b88f28f467612/flightBudget/prices"
HEADER = {
    "Authorization": TOKEN
}

class DataManager:
    """This class is responsible for getting and putting into a google sheet using the sheety API"""

    def getdata(self):
        """This method returns the values in a google sheet"""
        response = requests.get(url=ENDPOINT, headers=HEADER)
        response.raise_for_status()
        return response.json()["prices"]

    def update_iataCode(self, data: dict):
        """This method updates the iataCode in a google sheet, requires a dictionary with 'id' and 'iataCode' """
        parameters = {
            "price": {
                "iataCode": data["iataCode"]
            }
        }
        response = requests.put(url=f"{ENDPOINT}/{data['id']}", headers=HEADER, json=parameters)
        response.raise_for_status()
        print(response.text)

