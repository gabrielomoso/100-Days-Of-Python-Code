##################### Extra Hard Starting Project ######################

import datetime as dt
from random import randint
import smtplib
import pandas


def send_letter(receiver_email, letter, sender_email="", password="", ): #Remember to fill in the sender_email and password variables before running the code
    """This function sends a mail.
        Required values: receiver"s email, letter.
        Default values: sender_email, password.
        """


    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:  #The SMTP is set for yahoo mail... remember to check this before using
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(from_addr=sender_email, to_addrs=receiver_email,
                            msg=f"Subject: Happy Birthday \n\n{letter}")


now = dt.datetime.now()

birthdays = pandas.read_csv("birthdays.csv")  # Reading the birthdays from the csv file
for (index, values) in birthdays.iterrows():  # Looping through each birthdays
    if f"{now.date()}" == f"{values.year}-{values.month}-{values.day}":  # Checking if a date in the file match the present day
        with open(f"letter_templates/letter_{randint(1, 3)}.txt") as data:  # Getting a random letter from the available
            letter = data.read().replace("[NAME]", values["name"])  # replacing the word in the letter
            send_letter(receiver_email=values["email"],
                        letter=letter)  # sending a mail by calling the send_letter() function
