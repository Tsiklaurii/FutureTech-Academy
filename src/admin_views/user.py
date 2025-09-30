from os import path
from uuid import uuid4
from flask_admin.form import ImageUploadField
from markupsafe import Markup
from src import Config
from src.admin_views.base import SecureModelView
from wtforms.fields import SelectField

def generate_filename(obj, file):
    name, extension = path.splitext(file.filename)
    return f"{uuid4()}{extension}"

class UserView(SecureModelView):
    create_modal = True
    edit_modal = True
    can_view_details = True
    column_exclude_list = ['_password',]
    column_searchable_list = ['username', 'role']

    column_formatters = {
        'profile_img': lambda v, c, m, n: Markup(f"<img src='/static/upload/{m.profile_img}' width=70/>")
    }
    form_overrides = {"role": SelectField, "profile_img": ImageUploadField}
    form_args = {"role":{
        "choices":["Admin", "User"]},
        "img": {
            "base_path": Config.UPLOAD_PATH,
            "namegen": generate_filename
        }
    }
