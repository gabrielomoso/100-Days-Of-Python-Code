import requests
from datetime import datetime
import smtplib



# Go into this site to get your location data https://www.latlong.net/
MY_LAT = 6.524379  # Your latitude
MY_LONG = 3.379206  # Your longitude


def send_letter(receiver_email, sender_email,
                password):  # Remember to fill in the sender_email and password variables before running the code
    """This function sends a mail.
        Required values: receiver"s email, sender_email, password.
        """

    with smtplib.SMTP(
            "smtp.mail.yahoo.com") as connection:  # The SMTP is set for yahoo mail... remember to check this before using
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(from_addr=sender_email, to_addrs=receiver_email,
                            msg=f"Subject: The ISS is near you \n\n Look UP")


def is_near_me():
    """This function checks if the ISS is close to your location, Requires the correct constants in the file"""

    # Requesting a data from the ISS api
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    # Gets the current location of the ISS
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # checks if Your position is within +5 or -5 degrees of the ISS position.
    is_long = iss_longitude >= MY_LONG - 5 and iss_longitude <= MY_LONG + 5
    is_lat = iss_latitude >= MY_LAT - 5 and iss_latitude <= MY_LAT + 5

    if is_long and is_lat:
        return True


def is_dark():
    """This function checks if it is currently dark in your location, Requires the correct constants in the file"""

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    my_hour = time_now.hour
    return my_hour >= sunset + 3 and my_hour - 24 <= sunrise


if is_near_me() and is_dark():
    send_letter(receiver_email="", sender_email="", password="")  # Remember to fill this in for the code to work
