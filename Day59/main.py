from flask import Flask, render_template
import requests

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
response.raise_for_status()

blogs = response.json()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", blogs=blogs)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post/<num>")
def get_post(num):
    return render_template("post.html", blog=blogs[int(num) - 1])


if __name__ == "__main__":
    app.run(debug=True)
