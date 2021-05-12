import requests

"""
Client.py defines the classes that contains song information
"""

class Song(object): 
    def __init__(self, lastfm_json):
        self.title = lastfm_json['name']
        self.artist = lastfm_json['artist']
        self.mbid = lastfm_json['mbid']
        self.num_listeners = lastfm_json['listeners']
        self.url = lastfm_json['url']
    
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
            result.append(Song(item_json))

        return result

    def search_by_artist(self, search_artist):
        """
        Searches the API for the supplied search_artist.
        Returns a list of Song objects if the search was successful, or the error response if the search failed.

        Only use this method if the user is using the search bar on the website
        """
        pass