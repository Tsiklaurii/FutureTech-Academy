from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, FloatField
from flask_wtf.file import FileField, FileSize, FileAllowed

class CourseForm(FlaskForm):
    name = StringField("კურსის სახელი")
    price = FloatField("კურსის ფასი")
    prof = StringField("პროფესორის სახელი")
    img = FileField("პროფესორის ფოტო", validators=[FileSize(1024 * 1024), FileAllowed(["jpg", "png", "jpeg"])])
    date = StringField("კურსის ჩატარების თარიღი")
    description = StringField("კურსის აღწერა")
    submit = SubmitField("კურსის დამატება")