from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import current_user

from .. import bcrypt
from ..models import User
from ..forms import SearchForm

songs = Blueprint("songs", __name__)


""" ************ Song views ************ """


@songs.route("/", methods=["GET", "POST"])
def index():
    form = SearchForm()

    if form.validate_on_submit():
        # TODO: redirect to query_results() passing in data from form
        # TODO: actually show results
        return "you searched for: {}".format(form.search_query.data) 
    
    return render_template("index.html", form=form)

# TODO: def query_results()

# TODO: def song_detail()