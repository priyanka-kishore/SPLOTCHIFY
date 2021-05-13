from flask import Blueprint, redirect, url_for, render_template, flash, request
from flask_login import current_user, login_required, login_user, logout_user

from .. import bcrypt
from ..forms import RegistrationForm, LoginForm
from ..models import Comment, User

users = Blueprint("users", __name__)


""" ************ User Management views ************ """


@users.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        # return "you're logged in! pretend this is the song index" # TODO: redirect to song index
        return redirect(url_for("songs.index"))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hashed)
        user.save()
        print(" ~ ~ ~ USER SAVED.")
        return redirect(url_for("users.login")) # user must login after registering

    return render_template("register.html", title="Register", form=form)


@users.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("songs.index")) 

    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects(username=form.username.data).first()

        if user is not None and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("songs.index"))
        else:
            flash("Login failed. Check your username and/or password")
            return redirect(url_for("users.login"))

    return render_template("login.html", title="Login", form=form)
    

@users.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("users.login"))

@users.route("/profile/<user>", methods=["GET"])
@login_required
def profile(user):
    user_comments = Comment.objects(commenter=user)

    return render_template("profile.html", username=user, comments=user_comments)

# @users.route("/favorites", methods=["GET"])
# @login_required
# def get_favorites():
#     return "these are the songs with favorites, from the comment database"

# @users.route("/scores", methods=["GET"])
# @login_required
# def get_scores():
#     return "there are the songs with scores, from the comment database"