from src.admin_views.base import SecureModelView

class UserCourseView(SecureModelView):
    create_modal = True
    edit_modal = True

    form_columns = ["user", "course", "created_at"]
    column_list = ["id", "user", "course", "created_at"]