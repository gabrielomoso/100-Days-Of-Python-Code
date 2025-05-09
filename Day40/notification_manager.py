from data_manager import DataManager
from datetime import datetime
from dateutil.relativedelta import relativedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

PASSWORD = ""
SENDER = ""

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

        message_body = f"Only ₦{round(flight['price'])} to fly from {flight['cityFrom']}-{flight['cityCodeFrom']} to {flight['cityTo']}-{flight['cityCodeTo']} and back!, from {date_str} to {end_date}, link: {flight['deep_link']}"

        data_manager = DataManager()
        users = data_manager.getusers()
        for user in users:
            message = MIMEMultipart()
            message['From'] = SENDER
            message['To'] = user["email"]
            message['Subject'] = "We have a match for a nice flight!!"
            body = f"Dear {user['lastName']} {user['firstName']}\n{message_body}"
            message.attach(MIMEText(body, 'plain'))

            try:
                # Connect to the SMTP server
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    # Start TLS for security
                    connection.starttls()

                    # Login to the email account
                    connection.login(user=SENDER, password=PASSWORD)

                    # Send the email
                    connection.sendmail(from_addr=SENDER, to_addrs=user["email"], msg=message.as_string())

                print("Email sent successfully!")

            except smtplib.SMTPException as e:
                print(f"Error sending email to {user['email']}: {e}")
                # You can choose to log the error or take other appropriate actions

            except Exception as e:
                print(f"Unexpected error: {e}")
                # Handle other unexpected errors

