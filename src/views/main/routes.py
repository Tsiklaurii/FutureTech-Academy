from flask import Blueprint, render_template
from src.models.course import Course

main_blueprint = Blueprint("main", __name__)

@main_blueprint.route("/")
def index():
    courses = Course.query.all()
    return render_template("main/index.html", courses=courses)

@main_blueprint.route("/about")
def about():
    return render_template("main/about.html")

@main_blueprint.route("/blog")
def blog():
    return render_template("main/blog.html")

@main_blueprint.route("/blogdetails")
def blogdetails():
    return render_template("main/blogdetails.html")

@main_blueprint.route("/career")
def career():
    return render_template("main/career.html")

@main_blueprint.route("/contact")
def contact():
    return render_template("main/contact.html")