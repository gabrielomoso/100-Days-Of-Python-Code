import requests
from datetime import datetime
ID = ""
TOKEN = ""
API_KEY = ""
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/60e4509708e197940c7b88f28f467612/myWorkout/workouts"


def nutrionix():
    # gender = input("Gender: ")
    # weight = input("Weight in kg: ")
    # height = str(2.54 * float(input("Height in Inches: ")))
    # age = input("Age: ")
    query = input("What exercise did you do? ")

    header = {
        "x-app-id": ID,
        "x-app-key": API_KEY,
        "x-remote-user-id": "0"
    }

    parameters = {
        "query": query,
        "gender": "male",
        "weight_kg": "73.33",
        "height_cm": "15.49",
        "age": "21"
    }
    response = requests.post(url=NUTRITIONIX_ENDPOINT, json=parameters, headers=header)
    response.raise_for_status()
    return response.json()["exercises"][0]

def sheety(data):
    now = datetime.now()

    header = {
        "Authorization": TOKEN
    }
    parameters = {
        "workout": {
            "date": now.date().strftime("%d/%m/%y"),
            "time": now.time().strftime("%X"),
            "exercise": data["user_input"].title(),
            "duration": data["duration_min"],
            "calories": data["nf_calories"]
        }
    }

    response = requests.post(url=SHEETY_ENDPOINT, json=parameters, headers=header)
    response.raise_for_status()
    print(response.text)

sheety(nutrionix())


