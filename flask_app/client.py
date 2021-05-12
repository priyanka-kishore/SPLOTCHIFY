import requests

"""
Client.py defines the classes that contains song information
"""

class Song(object): 
    def __init__(self, lastfm_json):
        print(" ~ ~ init_song ~ ~")
        print(lastfm_json)
        self.title = lastfm_json['name']
        self.artist = lastfm_json['artist']
        self.num_listeners = lastfm_json['listeners']
        self.url = lastfm_json['url']
        if lastfm_json['mbid']:
            self.mbid = lastfm_json['mbid']
        else: # generate new mbid
            self.mbid = 'splotchify_id..{title}..{artist}'.format(title=self.title, artist=self.artist)
    
    def __repr__(self):
        return "{title} -- {artist}".format(title=self.title, artist=self.artist)

class SongClient(object):
    def __init__(self, api_key):
        self.sess = requests.Session()
        self.url = f"http://ws.audioscrobbler.com/2.0/?api_key={api_key}&format=json&"
    
    def search_by_song(self, search_string):
        """
        Searches the API for the supplied search_string.
        Returns a list of Song objects if the search was successful, or the error response if the search failed.

        Only use this method if the user is using the search bar on the website
        """
        print("SEARCH-BY-SONG")

        # parse string from search bar
        search_string = "+".join(search_string.split())
        page = 1

        # prepare url and get response from api
        search_url = f"method=track.search&track={search_string}&page={page}"
        resp = self.sess.get(self.url + search_url)
        if resp.status_code != 200:
            raise ValueError("Search request failed; Ensure correct API key")
        data = resp.json()

        # errors from response
        if not data['results']:
            raise ValueError(f'[ERROR]: Error retrieving results: \'{data["Error"]}\' ')

        # if not data['results']['opensearch:totalResults'] == 0:
        #     return 'NO RESULTS. WOULD YOU LIKE TO ADD THIS SONG?' # TODO: take users to add song page

        # parse response
        results_json = data['results']['trackmatches']['track'] # 30 per page
        remaining_results = int(data['results']['opensearch:totalResults'])

        result = []

        # TODO: pagination -- We may have more results than are first displayed
        # while remaining_results != 0:
        #     for item_json in results_json:
        #         result.append(Song(item_json))
        #         remaining_results -= len(results_json)
            
        #     page += 1
        #     print("page = {}".format(page))

        #     search_url = f"method=track.search&track={search_string}&page={page}"
        #     resp = self.sess.get(self.url + search_url)
        #     if resp.status_code != 200 or not resp.json()['results']:
        #         break
        #     results_json = data['results']['trackmatches']['track']

        for item_json in results_json:
            print(item_json)
            result.append(Song(item_json))

        return result


    def get_song_info(self, song_id):
        """
        Returns a Song object from the database, or the error response if the retrieval fails.
        """
        print(" - = GETTING SONG ID {} = -".format(song_id))

        song_data = {
            "name": None,
            "artist": None,
            # basic data ^ ----------
            "listeners": None,
            "playcount": None,
            "album_title": None
        }

        # just grab song name and artist if no page exists for them
        if (song_id.split('..')[0] == 'splotchify_id'): 
            song_data['name'] = song_id.split('..')[1]
            song_data['artist'] = song_id.split('..')[2]

            return song_data
        else:
            song_url = self.url + f"method=track.getInfo&mbid={song_id}"
            resp = self.sess.get(song_url)
            if resp.status_code != 200:
                raise ValueError("Search request failed; Ensure correct API key")
            data = resp.json()

            # errors from response
            if 'error' in data:
                raise ValueError(f'[ERROR]: Error retrieving results: \'{data["message"]}\'')

            song_data['name'] = data['track']['name']
            song_data['artist'] = data['track']['artist']['name']
            song_data['listeners'] = '{:,}'.format(int(data['track']['listeners']))
            song_data['playcount'] = '{:,}'.format(int(data['track']['playcount']))
            song_data['album_title'] = data['track']['album']['title']

            return song_data

    def get_lyrics(self, song):
        pass

        




