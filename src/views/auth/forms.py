from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, length, equal_to, ValidationError
from flask_wtf.file import FileField, FileRequired, FileSize, FileAllowed
from string import ascii_uppercase, ascii_lowercase, digits, punctuation

class RegisterForm(FlaskForm):
    username = StringField("მომხმარებლის სახელი", validators=[DataRequired()])
    email = StringField("ემაილი", validators=[DataRequired()])
    password = PasswordField("პაროლი",
                             validators=[DataRequired(),
                                         length(min=8, max=64)])
    repeat_password = PasswordField("გაიმეორეთ პაროლი",
                                    validators=[DataRequired(),
                                                equal_to("password",
                                                         message="პაროლები არ ემთხვევა!")])
    profile_image = FileField("პროფილის ფოტო",
                              validators=[FileSize(1024 * 1024),
                                          FileAllowed(["jpg", "png", "jpeg"])])
    agree = BooleanField('I agree to the terms and conditions.', validators=[DataRequired()])

    submit = SubmitField("რეგისტრაცია")

    def validate_password(self, field):
        contains_uppercase = False
        contains_lowercase = False
        contains_digits = False
        contains_symbols = False

        for char in field.data:
            if char in ascii_uppercase:
                contains_uppercase = True

            if char in ascii_lowercase:
                contains_lowercase = True

            if char in digits:
                contains_digits = True

            if char in punctuation:
                contains_symbols = True

        if not contains_uppercase:
            raise ValidationError("პაროლი უნდა შეიცავდეს დიდ ასოებს!")

        if not contains_lowercase:
            raise ValidationError("პაროლი უნდა შეიცავდეს პატარა ასოებს!")

        if not contains_digits:
            raise ValidationError("პაროლი უნდა შეიცავდეს რიცხვებს!")

        if not contains_symbols:
            raise ValidationError("პაროლი უნდა შეიცავდეს სიმბოლოებს!")