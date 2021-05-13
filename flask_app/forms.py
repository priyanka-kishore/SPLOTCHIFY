from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from wtforms import StringField, IntegerField, SubmitField, TextAreaField, PasswordField, BooleanField, FieldList
from wtforms.validators import (
    InputRequired,
    DataRequired,
    NumberRange,
    Length,
    Email,
    EqualTo,
    ValidationError,
)

from .models import User


"""
Search form to query database for specific songs
- Song title
"""
class SearchForm(FlaskForm):
    search_query = StringField(
        "Query", validators=[InputRequired(), Length(min=1, max=100)]
    )
    submit = SubmitField("Search")

"""
CommentForm to comment on and favorite specific songs
"""
class SongCommentForm(FlaskForm):
    text = TextAreaField("What do you think?", validators=[InputRequired(), Length(min=5, max=500)])
    favorited = BooleanField(default=True)
    submit = SubmitField("Comment")

"""
Registration form for users to create an account:
- Username
- Email
- Password
- Confirm Password
"""
class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", validators=[InputRequired(), Length(min=1, max=40)]
    )
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[InputRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.objects(username=username.data).first()
        if user is not None:
            raise ValidationError("Username is taken")

    def validate_email(self, email):
        user = User.objects(email=email.data).first()
        if user is not None:
            raise ValidationError("Email is taken")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Login")


class PlaylistForm(FlaskForm):
    name = StringField("Name of playlist", validators=[InputRequired(), Length(min=1, max=40)])
    description = StringField("Description of your playlist", validators=[Length(min=1, max=100)])
    create = SubmitField("Create playlist")

# class UpdateUsernameForm(FlaskForm):
#     username = StringField(
#         "Username", validators=[InputRequired(), Length(min=1, max=40)]
#     )
#     submit = SubmitField("Update Username")

#     def validate_username(self, username):
#         if username.data != current_user.username:
#             user = User.objects(username=username.data).first()
#             if user is not None:
#                 raise ValidationError("That username is already taken")
