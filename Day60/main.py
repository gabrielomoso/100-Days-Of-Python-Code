from flask import Flask, render_template, request
from email_sender import EmailSender
import requests

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
response.raise_for_status()

blogs = response.json()

app = Flask(__name__)
email_sender = EmailSender()


@app.route("/")
def home():
    return render_template("index.html", blogs=blogs)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    contact_message = ""
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone_number = request.form["phone_number"]
        message = request.form["message"]
        print(name, email, phone_number, message)
        email_sender.send_email(name=name, recipient_email=email, phone_number=phone_number, message=message)
        contact_message = "Successfully Sent Your Message"

    return render_template("contact.html", message=contact_message)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post/<num>")
def get_post(num):
    return render_template("post.html", blog=blogs[int(num) - 1])


if __name__ == "__main__":
    app.run(debug=True)
