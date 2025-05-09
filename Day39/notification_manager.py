import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from twilio.rest import Client

ACCOUNT_SID = ""
AUTH_TOKEN = ""
SEND_TO = ''

class NotificationManager:
    """This class sends SMS using the twilio API"""

    def send_notification(self, flight):
        """This method sends a notification by SMS, requires flight details"""


        # Extract the date from "local_departure"
        date_str = flight["local_departure"].split("T")[0]

        # Convert the date string to a datetime object
        date_format = "%Y-%m-%d"
        departure_date = datetime.strptime(date_str, date_format)


        # Calculate the end date based on the specified number of nights
        end_date = departure_date + relativedelta(days=+flight["nightsInDest"])


        client = Client(ACCOUNT_SID, AUTH_TOKEN)

        message = client.messages \
            .create(
            body=f"We have a match! Only ₦{round(flight['price'])} to fly from {flight['cityFrom']}-{flight['cityCodeFrom']} to {flight['cityTo']}-{flight['cityCodeTo']} and back!, from {date_str} to {end_date}, link: {flight['deep_link']}",
            from_="+12563051946",
            to=SEND_TO,
        )
        print(message.status)




