from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email, length
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField(label="Submit Post")


# TODO: Create a RegisterForm to register new users
class RegisterForm(FlaskForm):
    username = StringField(label="User Name", validators=[DataRequired(), length(min=3)])
    email = StringField(label="Email",
                        validators=[DataRequired(), Email(message="Please enter a valid email address.")])
    password = PasswordField(label="Password", validators=[DataRequired(), length(min=8)])
    submit = SubmitField(label="Register")


# TODO: Create a LoginForm to login existing users
class LoginForm(FlaskForm):
    email = StringField(label="Email",
                        validators=[DataRequired(), Email(message="Please enter a valid email address.")])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Let me in")


# TODO: Create a CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    comment = CKEditorField(label="Comment", validators=[DataRequired(), length(min=4)])
    submit = SubmitField(label="Submit")
