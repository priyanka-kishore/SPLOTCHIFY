from flask_app.utils import current_time
from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import current_user

from .. import song_client
from ..models import Comment, User
from ..forms import SearchForm, SongCommentForm

songs = Blueprint("songs", __name__)


""" ************ Song views ************ """


@songs.route("/", methods=["GET", "POST"])
def index():
    form = SearchForm()

    if form.validate_on_submit():
        return redirect(url_for("songs.song_query_results", query=form.search_query.data))
    
    return render_template("index.html", form=form)


@songs.route("/search-song/<query>", methods=["GET"])
def song_query_results(query):
    try:
        results = song_client.search_song(query)
    except ValueError as e:
        flash(str(e))
        return redirect(url_for("songs.index")) # go back to search form

    # return "your results: {}".format(results)
    return render_template("query.html", results=results)


@songs.route("/song/<song_id>", methods=["GET", "POST"])
def song_detail(song_id):
    print("LOOKING FOR: {}".format(song_id))
    song_info = song_client.get_song_info(song_id)
    print(song_info)

    form = SongCommentForm()
    if form.validate_on_submit() and current_user.is_authenticated:
        comment = Comment(
            commenter=current_user._get_current_object(),
            favorite=form.favorited.data,
            content=form.text.data,
            date=current_time(),
            song_id=song_id,
            song_title=song_info['name'],
            song_artist=song_info['artist']
        )
        comment.save() # save user's new comment if submitted!
        return redirect(request.path) # reload page

    comments = Comment.objects(song_id=song_id)

    return render_template("song_detail.html", form=form, song_info=song_info, comments=comments)

@songs.route("/create-playlist", methods=["GET"])
def create_playlist():
    return "here's the create a playlist form!"