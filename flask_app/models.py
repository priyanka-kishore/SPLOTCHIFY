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
    """
    A user registered with the system
    """
    username = db.StringField(required=True, unique=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)

    # Returns unique string identifying our object
    def get_id(self):
        return self.username

class Score(db.Document):
    """
    A score for that a user received for a song
    """
    username = db.ReferenceField(User, required=True)
    song_id = db.StringField(required=True)
    song_title = db.StringField(required=True, min_length=1, max_length=100)
    song_artist = db.StringField(required=True, min_length=1, max_length=100)
    score = db.IntField(required=True, default=0)

class Comment(db.Document):
    """
    A comment on a song submitted by a user
    """
    commenter = db.StringField(required=True)
    favorite = db.BooleanField(required=True, default=False)
    content = db.StringField(required=True, min_length=5, max_length=500)
    date = db.StringField(required=True)
    song_id = db.StringField(required=True)
    song_title = db.StringField(required=True, min_length=1, max_length=100)
    song_artist = db.StringField(required=True, min_length=1, max_length=100)

class Playlist(db.Document):
    """
    A playlist of songs created by the user
    """
    user = db.ReferenceField(User, required=True)
    songs = db.ListField(db.StringField()) # of song_ids?