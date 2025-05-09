from flask import Flask, render_template
from post import Post

app = Flask(__name__)
post = Post()


@app.route('/')
def home():
    blogs = post.all_post()
    return render_template("index.html", blogs=blogs)


@app.route("/blog/<num>")
def get_blog(num):
    blog = post.get_post(post_number=int(num) - 1)
    return render_template("post.html", blog=blog)


if __name__ == "__main__":
    app.run(debug=True)
