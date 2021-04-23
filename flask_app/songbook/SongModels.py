"""
A Song object to store song information.
"""
class Song(object):
    def __init__(self, id, title, artist):
        self.id = id # ideally, songbook's count
        self.title = title
        self.artist = artist


"""
A SongBook object to store many songs.
"""
class SongBook(object):
    def __init__(self):
        self.count = 0
        self.list = [] # of Song objects
    
    # add_song

    # delete_song
    
    # get_song_by_id
    # get_songs_by_artist
    # get_songs_by_title