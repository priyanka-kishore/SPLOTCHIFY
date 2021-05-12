from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import current_user

from .. import song_client
from ..models import User
from ..forms import SearchForm

songs = Blueprint("songs", __name__)


""" ************ Song views ************ """


@songs.route("/", methods=["GET", "POST"])
def index():
    form = SearchForm()

    if form.validate_on_submit():
        return redirect(url_for("songs.song_query_results", query=form.search_query.data))
        # TODO: actually show results
        # return "you searched for: {}".format(form.search_query.data) 
    
    return render_template("index.html", form=form)


@songs.route("/search-song/<query>", methods=["GET"])
def song_query_results(query):
    try:
        results = song_client.search_by_song(query)
    except ValueError as e:
        flash(str(e))
        return redirect(url_for("songs.index")) # go back to search form

    # return "your results: {}".format(results)
    return render_template("query.html", results=results)


# TODO
# @songs.route("/search-artist/<query>", methods=["GET"])
# def artist_query_results(query):
#     try:
#         results = song_client.search_by_artist(query)
#     except ValueError as e:
#         flash(str(e))
#         return redirect(url_for("songs.index")) # go back to search form

#     return "your results: {}".format(results)
#     # return render_template("query.html", results=results)


@songs.route("/song/<song_id>", methods=["GET"])
def song_detail(song_id):
    print("LOOKING FOR: {}".format(song_id))
    song_info = song_client.get_song_info(song_id)
    return song_info