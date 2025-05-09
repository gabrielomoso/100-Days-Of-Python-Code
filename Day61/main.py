from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

login = {
    "email": "",
    "password": ""  # Changed to string
}

class LoginForm(FlaskForm):
    name = StringField(label="Name", validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email(message="Invalid email address")])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8, message="Make sure the field is at least 8 characters long")])
    submit = SubmitField(label="Log in")

app = Flask(__name__)
app.secret_key = ""
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login_handler():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == login["email"] and form.password.data == login["password"]:
            return render_template("success.html", name=form.name.data)
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
