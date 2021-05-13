# 3rd-party packages
from flask import Flask, render_template, request, redirect, url_for
from flask_mongoengine import MongoEngine
from flask_login import (
    LoginManager,
    current_user,
    login_user,
    logout_user,
    login_required,
)
from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename
from flask_mail import Mail

# stdlib
from datetime import datetime
import os

# local
from .client import SongClient


db = MongoEngine()
login_manager = LoginManager()
bcrypt = Bcrypt()
song_client = SongClient(os.environ.get("LASTFM_API_KEY"))
mail = Mail()


# from .routes import main
from .users.routes import users
from .songs.routes import songs


def page_not_found(e):
    return render_template("404.html"), 404


def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_pyfile("config.py", silent=False)
    if test_config is not None:
        app.config.update(test_config)

    # app.config['MAIL_PASSWORD'] = '$pL0tch1f4' # os.environ.get("MAIL_PASSWORD")
    # app.config['MAIL_USERNAME'] = 'splotchifyapp@gmail.com' # os.environ.get("MAIL_SENDER")
    # app.config['MAIL_PORT'] = 25

    mail.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    

    app.register_blueprint(users)
    app.register_blueprint(songs)
    app.register_error_handler(404, page_not_found)

    login_manager.login_view = "main.login"

    return app
