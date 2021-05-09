import requests

url = "https://shazam.p.rapidapi.com/search"

querystring = {"term":"kiss the rain","locale":"en-US","offset":"0","limit":"5"}

headers = {
    'x-rapidapi-key': "0138139d1fmsh24d2c93a6d0f196p1aa90fjsn3189f2c2a2a5",
    'x-rapidapi-host': "shazam.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)