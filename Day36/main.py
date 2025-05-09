import requests
from datetime import datetime, timedelta
from twilio.rest import Client
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Get the current date and time
current_date = datetime.now()

# Calculate the date of the previous day
yesterday = (current_date - timedelta(days=1)).strftime("%Y-%m-%d")
today = current_date.strftime("%Y-%m-%d")

NEWS_API_KEY = ""
ALPHAVANTAGE_API_KEY = ""

TWILIO_ACCOUNT_SID = ""
TWILIO_AUTH_TOKEN = ""

EMAIL_PASSWORD = ""
SENDER_EMAIL = ""
RECEIVER_EMAIL = ""


def eurusd_forex_news():
    """This function sends forex news as a text message"""

    # Necessary parameters for the newsapi
    parameters = {
        "q": "EUR/USD",
        "from": yesterday,
        "language": "en",
        "apiKey": NEWS_API_KEY
    }

    #Getting the data from the API
    response = requests.get("https://newsapi.org/v2/everything", params=parameters)
    response.raise_for_status()
    news_articles = response.json()["articles"]

    # Initializing a message body
    message_body = f"{stats}\n\n"

    # Concatenating the title, URL, and content of each article into the message body
    for article in news_articles:
        title = article["title"]
        content = article.get("content", "No content available.")
        url = article["url"]
        message_body += f"Title: {title}\nURL: {url}\nContent: {content}\n\n"

    # Sending the message using the Twilio API
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages \
        .create(
        body=message_body,
        from_="+12563051946",
        to='+2347042011076',
    )

    print(message.status)


def eur_and_usd_news():
    """This function sends forex news as an email"""

    # Necessary parameters for the newsapi
    parameters = {
        "q": "EUR USD",
        "from": yesterday,
        "language": "en",
        "apiKey": NEWS_API_KEY
    }

    response = requests.get("https://newsapi.org/v2/everything", params=parameters)
    response.raise_for_status()
    articles = response.json()["articles"]
    news_articles = []

    #Only 10 articles max are required
    if len(articles) > 10:
        news_articles = articles[:10]

    # Initializing a message body
    message_body = f"{stats}\n\n"


    # Concatenate the title, URL, and content of each article into the message body
    for article in news_articles:
        title = article["title"]
        content = article.get("content", "No content available.")
        url = article["url"]

        message_body += f"Title: {title}\nURL: {url}\nContent: {content}\n\n"

    # Send the message as an email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=EMAIL_PASSWORD)

        # Create a MIMEMultipart object for the email message
        msg = MIMEMultipart()

        # Attach text content
        msg.attach(MIMEText(message_body, 'plain'))

        # Set the email subject and sender/receiver email addresses
        msg['Subject'] = 'EUR/USD News Update'
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL

        # Send the email
        connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=RECEIVER_EMAIL, msg=msg.as_string())


def fx_stats():
    """This function returns the stats of the EUR/USD pair"""
    parameters = {
        "function": "FX_DAILY",
        "from_symbol": "EUR",
        "to_symbol": "USD",
        "apikey": ALPHAVANTAGE_API_KEY
    }
    response = requests.get("https://www.alphavantage.co/query?", params=parameters)
    response.raise_for_status()
    daily_fx = response.json()["Time Series FX (Daily)"]
    today_price = float(daily_fx[today]["1. open"])
    yesterday_price = float(daily_fx[yesterday]["1. open"])
    difference = today_price - yesterday_price
    percent = round((difference / today_price) * 100, 3)
    if percent > 0:
        status = "UP by 🔼"
    else:
        status = "Down by 🔻"
    return f"The EUR/USD has gone {status} {percent}"


stats = fx_stats()
eurusd_forex_news()
eur_and_usd_news()
