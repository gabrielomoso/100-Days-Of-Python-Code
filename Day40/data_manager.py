import requests

TOKEN = ""
ENDPOINT = "https://api.sheety.co/60e4509708e197940c7b88f28f467612/flightBudget"
HEADER = {
    "Authorization": TOKEN
}

class DataManager:
    """This class is responsible for getting and putting into a google sheet using the sheety API"""

    def getprices(self):
        """This method returns the prices in a google sheet"""
        response = requests.get(url=f"{ENDPOINT}/prices", headers=HEADER)
        response.raise_for_status()
        return response.json()["prices"]


    def getusers(self):
        """This method returns the users in a google sheet"""
        response = requests.get(url=f"{ENDPOINT}/users", headers=HEADER)
        response.raise_for_status()
        return response.json()["users"]



    def update_iataCode(self, data: dict):
        """This method updates the iataCode in a google sheet, requires a dictionary with 'id' and 'iataCode' """
        parameters = {
            "price": {
                "iataCode": data["iataCode"]
            }
        }
        response = requests.put(url=f"{ENDPOINT}/prices/{data['id']}", headers=HEADER, json=parameters)
        response.raise_for_status()
        print(response.text)


    def update_lowestprice(self, data: dict):
        """This method updates the lowest price in the google sheet"""
        parameters = {
            "price": {
                "lowestPrice": data["lowestPrice"]
            }
        }
        response = requests.put(url=f"{ENDPOINT}/prices/{data['id']}", headers=HEADER, json=parameters)
        response.raise_for_status()
        print(response.text)


    def add_user(self, firstname, lastname, email):
        """This method adds a new user to the google sheets, requires firstname, lastname and email"""
        parameters = {
            "user": {
                "firstName": firstname,
                "lastName": lastname,
                "email": email
            }
        }

        response = requests.post(url=f"{ENDPOINT}/users", headers=HEADER, json=parameters)
        response.raise_for_status()
        print(response.text)

