def send_email(subject, stats, news_articles, image_attachments=[]):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=EMAIL_PASSWORD)

        msg = MIMEMultipart()

        # Attach stats
        msg.attach(MIMEText(stats, 'plain'))

        # Attach news articles
        for article in news_articles:
            title = article["title"]
            content = article.get("content", "No content available.")
            url = article["url"]
            message_body = f"Title: {title}\nURL: {url}\nContent: {content}\n\n"
            msg.attach(MIMEText(message_body, 'plain'))

        # Attach image attachments
        for image_attachment in image_attachments:
            msg.attach(image_attachment)

        msg['Subject'] = subject
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL

        connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=RECEIVER_EMAIL, msg=msg.as_string())
