from flask_login import UserMixin
from datetime import datetime
from . import db, login_manager
from . import config
from .utils import current_time
import base64

"""
This are models that stored in the MongoDB database!
"""


@login_manager.user_loader
def load_user(user_id):
    return User.objects(username=user_id).first()

class User(db.Document, UserMixin):
    username = db.StringField(required=True, unique=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)

    # Returns unique string identifying our object
    def get_id(self):
        return self.username


class Comment(db.Document):
    """
    A comment on a song submitted by a user
    """
    commenter = db.ReferenceField(User, required=True)
    favorite = db.BooleanField(required=True, default=False)
    content = db.StringField(required=True, min_length=5, max_length=500)
    date = db.StringField(required=True)
    song_id = db.StringField(required=True)
    song_title = db.StringField(required=True, min_length=1, max_length=100)
    song_artist = db.StringField(required=True, min_length=1, max_length=100)