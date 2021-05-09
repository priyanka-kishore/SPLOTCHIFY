import requests

url = "https://theaudiodb.p.rapidapi.com/search.php"

querystring = {"s":"coldplay"}

headers = {
    'x-rapidapi-key': "a96fd0e7femsh4e6017c74d0e8e2p1add38jsn292d5c9a85bb",
    'x-rapidapi-host': "theaudiodb.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)