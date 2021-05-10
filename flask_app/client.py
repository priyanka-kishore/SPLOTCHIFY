import requests

"""
Client.py defines the classes that contains song information
"""

# DELETE 4e3cb83509f6bb0d13809776377788b9

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
        self.pre_url = f"http://ws.audioscrobbler.com/2.0/?"
        self.end_url = f"&api_key={api_key}&format=json"
        # http://ws.audioscrobbler.com/2.0/?  |   method={method}&track=Believe  |   &api_key=4e3cb83509f6bb0d13809776377788b9&format=json

    def search_by_song(self, search_string):
        """
        Searches the API for the supplied search_string, and returns a list of Song
        objects if the search was successful, or the error response if the search failed.

        Only use this method if the user is using the search bar on the website
        """

        # parse string from search bar
        search_string = "+".join(search_string.split()) # replace spaces with '+'

        search_url = f"method=track.search&track={search_string}"

        req = requests.Request("GET", url, params=searchstring).prepare()


    # maybe
    # def get_song_info(self, song):
    #     pass

# class MovieClient(object):
#     def __init__(self, api_key):
#         self.sess = requests.Session()
#         self.base_url = f"http://www.omdbapi.com/?apikey={api_key}&r=json&type=movie&"

#     def search(self, search_string):
#         """
#         Searches the API for the supplied search_string, and returns
#         a list of Media objects if the search was successful, or the error response
#         if the search failed.

#         Only use this method if the user is using the search bar on the website.
#         """
#         search_string = "+".join(search_string.split())
#         page = 1

#         search_url = f"s={search_string}&page={page}"

#         resp = self.sess.get(self.base_url + search_url)

#         if resp.status_code != 200:
#             raise ValueError(
#                 "Search request failed; make sure your API key is correct and authorized"
#             )

#         data = resp.json()

#         if data["Response"] == "False":
#             raise ValueError(f'[ERROR]: Error retrieving results: \'{data["Error"]}\' ')

#         search_results_json = data["Search"]
#         remaining_results = int(data["totalResults"])

#         result = []

#         ## We may have more results than are first displayed
#         while remaining_results != 0:
#             for item_json in search_results_json:
#                 result.append(Movie(item_json))
#                 remaining_results -= len(search_results_json)
#             page += 1
#             search_url = f"s={search_string}&page={page}"
#             resp = self.sess.get(self.base_url + search_url)
#             if resp.status_code != 200 or resp.json()["Response"] == "False":
#                 break
#             search_results_json = resp.json()["Search"]

#         return result

#     def retrieve_movie_by_id(self, imdb_id):
#         """
#         Use to obtain a Movie object representing the movie identified by
#         the supplied imdb_id
#         """
#         movie_url = self.base_url + f"i={imdb_id}&plot=full"

#         resp = self.sess.get(movie_url)

#         if resp.status_code != 200:
#             raise ValueError(
#                 "Search request failed; make sure your API key is correct and authorized"
#             )

#         data = resp.json()

#         if data["Response"] == "False":
#             raise ValueError(f'Error retrieving results: \'{data["Error"]}\' ')

#         movie = Movie(data, detailed=True)

#         return movie


# ## -- Example usage -- ###
# if __name__ == "__main__":
#     import os

#     client = MovieClient(os.environ.get("OMDB_API_KEY"))

#     movies = client.search("guardians")

#     for movie in movies:
#         print(movie)

#     print(len(movies))
