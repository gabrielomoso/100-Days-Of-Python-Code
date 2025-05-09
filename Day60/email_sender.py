import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

PASSWORD = ""
SENDER = ""

class EmailSender:
    def __init__(self):
        self.email = SENDER
        self.password = PASSWORD

    def send_email(self, name, phone_number, recipient_email, message):
        # Create a multipart message
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = recipient_email
        msg['Subject'] = 'New message from your website'

        # Add message body
        body = f"Name: {name}\nPhone Number: {phone_number}\n\nMessage:\n{message}"
        msg.attach(MIMEText(body, 'plain'))

        # Connect to SMTP server and send email
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.email, self.password)
            server.sendmail(self.email, recipient_email, msg.as_string())
            print("Email sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")
