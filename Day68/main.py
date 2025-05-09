from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = ''

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)

# Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


with app.app_context():
    db.create_all()


# Function to login in user and add its sessions
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        user = User.query.filter_by(email=email).scalar()

        if user:
            flash("User already in Database, Please Login")
            return redirect(url_for('login'))

        new_user = User(
            email=email,
            password=generate_password_hash(request.form.get("password"), salt_length=8, method="pbkdf2:sha256"),
            name=request.form.get("name")
        )
        db.session.add(new_user)
        db.session.commit()

        # Logging in user
        user_object = load_user(new_user.id)
        login_user(user_object)

        flash("Login successful")
        return redirect(url_for('secrets'))
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(email = request.form.get('email')).scalar()
        if user:
            if check_password_hash(pwhash=user.password, password=request.form.get('password')):

                # Logging in user
                user_object = load_user(user.id)
                login_user(user_object)
                flash("Logging successful")
                return redirect(url_for('secrets'))
            else:
                flash("Please Recheck password")
                return redirect(url_for('login'))
        else:
            flash("User not in Database")
            return redirect(url_for('login'))

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=current_user.is_authenticated)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory("static", "files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
