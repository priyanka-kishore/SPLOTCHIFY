import requests
import json

# DOCUMENTATION: https://www.last.fm/api/intro

url = "http://ws.audioscrobbler.com/2.0/?"
fmt = "json"
api_key = "4e3cb83509f6bb0d13809776377788b9"

"""
Search for a songs with similar name
"method=track.search&track=Believe&api_key=YOUR_API_KEY&format=json"
"""
searchstring = {
    "method": "track.search",
    "track": "Believe", # from user search bar
    "api_key": api_key,
    "format": fmt
}

sess = requests.Session()
req = requests.Request("GET", url, params=searchstring).prepare()
print(req.url)

# response = requests.request("GET", url, params=searchstring) # get data
response = sess.send(req)


data = json.loads(response.text) # convert string to json
tracks = data['results']['trackmatches']['track'] # get list of all related tracks
names = [(track['name'], track['artist']) for track in tracks] # make list of all (name, artist)

for t in names:
    print("{name} -- {artist}".format(name=t[0], artist=t[1]))
print("COUNT: {}".format(len(names)))


"""
LATER:
Search for top tracks BY an artist
artist.getTopTracks
"method=artist.gettoptracks&artist=cher&api_key=YOUR_API_KEY&format=json"
"""

