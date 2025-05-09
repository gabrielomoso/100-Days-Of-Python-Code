from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
CKEditor(app)
Bootstrap5(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


class NewBlog(FlaskForm):
    title = StringField(label="Blog Post Tile", validators=[DataRequired()])
    subtitle = StringField(label="Subtitle", validators=[DataRequired()])
    author = StringField(label="Your Name", validators=[DataRequired()])
    img_url = StringField(label="Blog Image Url", validators=[DataRequired()])
    body = CKEditorField(label="Blog Content", validators=[DataRequired()])
    submit = SubmitField(label="Submit")


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


# TODO: Add a route so that you can click on individual posts.
@app.route('/post<post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = BlogPost.query.get(post_id)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route('/new-post', methods=["GET", "POST"])
def add_new_post():
    new_blog = NewBlog()
    if new_blog.validate_on_submit():
        new_post = BlogPost(
            title=new_blog.title.data,
            subtitle=new_blog.subtitle.data,
            body=new_blog.body.data,
            author=new_blog.author.data,
            img_url=new_blog.img_url.data,
            date=datetime.now().strftime("%A %d,%Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))

    return render_template("make-post.html", form=new_blog)


# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<num>", methods=["GET", "POST"])
def edit_post(num):
    # Retrieve the existing blog post data
    blog_to_edit = BlogPost.query.get(num)

    # Create a NewBlog form instance
    edited_blog = NewBlog()

    if edited_blog.validate_on_submit():
        # Update the blog post with the form data
        blog_to_edit.title = edited_blog.title.data
        print(blog_to_edit.title)
        blog_to_edit.subtitle = edited_blog.subtitle.data
        blog_to_edit.body = edited_blog.body.data
        blog_to_edit.author = edited_blog.author.data
        blog_to_edit.img_url = edited_blog.img_url.data
        db.session.commit()
        return redirect(url_for('show_post', post_id=num))

    # Prepopulate form fields with existing data
    edited_blog.title.data = blog_to_edit.title
    edited_blog.subtitle.data = blog_to_edit.subtitle
    edited_blog.body.data = blog_to_edit.body
    edited_blog.author.data = blog_to_edit.author
    edited_blog.img_url.data = blog_to_edit.img_url

    return render_template("make-post.html", form=edited_blog, header="Edit Post")


# TODO: delete_post() to remove a blog post from the database
@app.route("/delete-post/<num>")
def delete_post(num):
    post_to_delete = BlogPost.query.get(num)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
