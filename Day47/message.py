import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



EMAIL_PASSWORD = "ilofnbbyemqxkduy"
SENDER_EMAIL = "gabzthebahdguy@gmail.com"
RECEIVER_EMAIL = "gabrielomoso@gmail.com"

class Message:
    def send_mail(self,name, price, link):
        message_body = f"{name} is now sold for ${price}.\n{link}"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=EMAIL_PASSWORD)

            # Create a MIMEMultipart object for the email message
            msg = MIMEMultipart()

            # Attach text content
            msg.attach(MIMEText(message_body, 'plain'))

            # Set the email subject and sender/receiver email addresses
            msg['Subject'] = 'AMAZON PRICE ALERT!'
            msg['From'] = SENDER_EMAIL
            msg['To'] = RECEIVER_EMAIL

            # Send the email
            connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=RECEIVER_EMAIL, msg=msg.as_string())

            print("Message sent successfully!")
