import requests
import os
from twilio.rest import Client

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
key = ""
parameters = {
    "lat": 0.0,
    "lon": 0.0,
    "appid": key,
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_data = weather_data["hourly"][:12]

will_rain = False

for item in hourly_data:
    hour_id = item["weather"][0]["id"]
    if hour_id > 700:
        will_rain = True

if will_rain:
    account_sid = ""
    auth_token = ""
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It will not rain today. We have clear Skys",
        from_="+12563051946",
        to='+2347042011076',
    )
    print(message.status)
