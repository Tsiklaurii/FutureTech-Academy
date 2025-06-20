from src.admin_views.base import SecureModelView
from src.config import Config

from flask_admin.form import ImageUploadField
from os import path
from uuid import uuid4

def generate_filename(obj, file):
    name, extension = path.splitext(file.filename)
    return f"{uuid4()}{extension}"

class CourseView(SecureModelView):

    create_modal = True
    edit_modal = True
    column_editable_list = _list = ("price",)
    column_filters = ("price", "name")

    form_overrides = {"img": ImageUploadField}
    form_args = {
        "img": {
            "base_path": Config.UPLOAD_PATH,
            "namegen": generate_filename
        }
    }