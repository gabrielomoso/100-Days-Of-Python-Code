import smtplib
import datetime as dt
from random import choice

sender_mail = ""
password = ""
receiver_mail = ""


now = dt.datetime.now()
day = now.weekday()
if day == 5:

    with open("qoutes.txt", encoding="utf-8") as data:
        quotes = data.readlines()
        quote = choice(quotes)

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=sender_mail, password=password)
        connection.sendmail(from_addr=sender_mail, to_addrs=receiver_mail, msg=f"Subject: Motivational Quote \n\n{quote}")





