from flask_app.utils import current_time
from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import current_user
from flask_mail import Message

from .. import song_client, mail
from ..models import Comment, User
from ..forms import SearchForm, SongCommentForm, PlaylistForm, SubmitSongForm

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
            commenter=current_user.username,
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
    # TODO: create a playlist of songs
    # form = PlaylistForm()
    # if form.validate_on_submit():
        # playlist = 
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

    return "here's the create a playlist form!"

@songs.route("/submit-song", methods=["GET", "POST"])
def submit_song():
    form = SubmitSongForm()

    if form.validate_on_submit():
        # send an email to the user about their request
        song_title = form.song_title.data
        song_artist = form.song_artist.data

        print("sending email about [{}] by [{}]...".format(song_title, song_artist))
        # mail testing (Remove)
        msg = Message("Thank you for your Splotchify song submission!", recipients=[current_user.email])
        msg.html = '''
            <h1>Hello, {username}!</h1>
            <br>
            <h2>Thank you for submitting a song to our Splotchify database.</h2>
            <br>
            <h3>You submitted:</h3>
            <p>Song: "{song}"</p>
            <p>Artist: "{artist}"</p>
            <br>
            <p>We will review your song submission and add it to the database once approved. Thank you for supporting and contributing to the Splotchify community!</p>
            <br>
            <p>From the Splotchify Team :)</p>
        '''.format(username=current_user.username, song=song_title, artist=song_artist)
        
        mail.send(msg)
        print("EMAIL SENT")

        return render_template("submit_song.html", form=form, email_sent=True, user_email=current_user.email)
        
    # return "this is where you submit a song to the database and you will receive an email confirming your request"
    return render_template("submit_song.html", form=form, email_sent=False, user_email=current_user.email)