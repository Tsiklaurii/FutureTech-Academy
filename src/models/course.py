from src.models.base import BaseModel
from src.ext import db

class Course(BaseModel):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    prof = db.Column(db.String(100))
    img = db.Column(db.String(300))
    description = db.Column(db.String(1000))
    date = db.Column(db.String(50))

    user_courses = db.relationship("UserCourse", back_populates="course")


    def __repr__(self):
        return self.name