from datetime import datetime
from src.models.base import BaseModel
from src.ext import db

class UserCourse(BaseModel):
    __tablename__ = "users_courses"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", back_populates="user_courses")
    course = db.relationship("Course", back_populates="user_courses")