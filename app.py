from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from forms import RegisterForm, CourseForm
from os import path
from uuid import uuid4

app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkeyyy1234@@@@"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
UPLOAD_PATH = path.join(app.root_path, "static", "upload")

db = SQLAlchemy(app)

# MODELS

class Course(db.Model):
    __tablename__ = "courses"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    prof = db.Column(db.String(100))
    img = db.Column(db.String(300))
    description = db.Column(db.String(1000))
    date = db.Column(db.String(50))


@app.route("/")
def index():
    courses = Course.query.all()
    return render_template("index.html", courses=courses)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/blogdetails")
def blogdetails():
    return render_template("blogdetails.html")

@app.route("/career")
def career():
    return render_template("career.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/registration", methods=["GET", "POST"])
def registration():
    form = RegisterForm()
    if form.validate_on_submit():
        file = form.profile_image.data

        _, extension = path.splitext(file.filename)
        filename = f"{uuid4()}{extension}"
        file.save(path.join(UPLOAD_PATH, filename))
    return render_template("registration.html", form=form)

@app.route("/add_course", methods=["GET", "POST"])
def add_product():
    form = CourseForm()
    if form.validate_on_submit():
        file = form.img.data
        _, extension = path.splitext(file.filename)
        filename = f"{uuid4()}{extension}"
        file.save(path.join(UPLOAD_PATH, filename))

        new_course = Course(name=form.name.data, price=form.price.data, prof=form.prof.data,
                            img=filename, description=form.description.data, date=form.date.data)
        db.session.add(new_course)
        db.session.commit()

        return redirect(url_for("index"))

    return render_template("add_course.html", form=form)

@app.route("/edit_course/<int:id>", methods=["GET", "POST"])
def edit_product(id):
    course = Course.query.get(id)
    form = CourseForm(name=course.name, price=course.price, prof=course.prof, description=course.description, date=course.date)

    if form.validate_on_submit():
        course.name = form.name.data
        course.price = form.price.data
        course.prof = form.prof.data
        course.description = form.description.data
        course.date = form.date.data

        if form.img.data:
            file = form.img.data
            _, extension = path.splitext(file.filename)
            filename = f"{uuid4()}{extension}"
            file.save(path.join(UPLOAD_PATH, filename))

            course.img = filename

        db.session.commit()
        return redirect(url_for("index"))

    return render_template("add_course.html", form=form)

@app.route("/delete_course/<int:id>")
def delete_course(id):
    course = Course.query.get(id)
    db.session.delete(course)
    db.session.commit()

    return redirect(url_for("index"))

@app.route("/view/<int:courses_id>")
def view_course(courses_id):
    chosen_course = Course.query.get(courses_id)
    return render_template("view_course.html", course=chosen_course)

if __name__ == "__main__":
    app.run(debug=True)