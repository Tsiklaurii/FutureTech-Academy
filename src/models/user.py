from flask_login import UserMixin

from src.ext import db
from src.models.base import BaseModel

class User(BaseModel, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    profile_img = db.Column(db.String)