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
        return "you're logged in! pretend this is the song index" # TODO: redirect to song index
        # return redirect(url_for("movies.index"))

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
        return "you're logged in! pretend this is the song index" # TODO: redirect to song index since already logged in
        # return redirect(url_for("movies.index")) 

    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects(username=form.username.data).first()

        if user is not None and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            print("~ ~ ~ USER LOGIN SUCCESS")
            return redirect(url_for("songs.index")) # TODO: redirect to song index after logging in
        else:
            flash("Login failed. Check your username and/or password")
            return redirect(url_for("users.login"))

    return render_template("login.html", title="Login", form=form)
    

@users.route("/logout")
@login_required
def logout():
    logout_user()
    print("~ ~ ~ USER LOGOUT SUCCESS")
    return redirect(url_for("users.login"))

@users.route("/profile/<user>", methods=["GET"])
@login_required
def profile(user):
    # TODO: create a playlist of songs
    # form = PlaylistForm()
    # if form.validate_on_submit():
        # comment = Comment(
        #     commenter=current_user._get_current_object(),
        #     favorite=form.favorited.data,
        #     content=form.text.data,
        #     date=current_time(),
        #     song_id=song_id,
        #     song_title=song_info['name'],
        #     song_artist=song_info['artist']
        # )
        # comment.save() # save user's new comment if submitted!
        # return redirect(request.path) # reload page

    user_comments = Comment.objects(commenter=current_user._get_current_object())

    return render_template("profile.html", username=current_user.username, comments=user_comments)