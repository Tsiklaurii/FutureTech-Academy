from uuid import uuid4
from os import path
from flask import Blueprint, render_template, url_for, redirect
from flask_login import login_required

from src.views.course.forms import CourseForm
from src.models.course import Course
from src.config import Config
from src.utils import admin_required

course_blueprint = Blueprint("courses", __name__)

@course_blueprint.route("/add_course", methods=["GET", "POST"])
@admin_required
def add_product():
    form = CourseForm()
    if form.validate_on_submit():
        file = form.img.data
        _, extension = path.splitext(file.filename)
        filename = f"{uuid4()}{extension}"
        file.save(path.join(Config.UPLOAD_PATH, filename))

        new_course = Course(name=form.name.data, price=form.price.data, prof=form.prof.data,
                            img=filename, description=form.description.data, date=form.date.data)
        new_course.create()

        return redirect(url_for("main.index"))

    return render_template("course/add_course.html", form=form)

@course_blueprint.route("/edit_course/<int:id>", methods=["GET", "POST"])
@admin_required
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
            file.save(path.join(Config.UPLOAD_PATH, filename))

            course.img = filename

        course.save()
        return redirect(url_for("main.index"))

    return render_template("course/add_course.html", form=form)

@course_blueprint.route("/delete_course/<int:id>")
@admin_required
def delete_course(id):
    course = Course.query.get(id)
    course.delete()

    return redirect(url_for("main.index"))

@course_blueprint.route("/view/<int:courses_id>")
def view_course(courses_id):
    chosen_course = Course.query.get(courses_id)
    return render_template("course/view_course.html", course=chosen_course)