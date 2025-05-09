from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)

class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    all_books = db.session.execute(db.select(Books).order_by(Books.id)).scalars()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        data = Books(
            title = request.form["name"],
            author = request.form["author"],
            rating = request.form["rating"]
        )
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("add.html")


@app.route("/edit/<num>", methods=["GET", "POST"])
def edit(num):
    book_to_update = db.session.execute(db.select(Books).where(Books.id == num)).scalar()
    if request.method == "POST":
        book_to_update.rating = request.form["new_rating"]
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", book=book_to_update)


@app.route("/delete/<num>")
def delete(num):
    book_to_delete = db.session.execute(db.select(Books).where(Books.id == num)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
