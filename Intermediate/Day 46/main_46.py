import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import info

client_id = info.client_id
client_secret = info.client_secret
redirect_uri = info.redirect_uri


date = input("Which date do you want to travel to? YYYY-MM-DD: ")


scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))


header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 OPR/119.0.0.0"}
url = "https://www.billboard.com/charts/hot-100/"+date
response = requests.get(url=url, headers=header)

content = response.text

soup = BeautifulSoup(content, "html.parser")

# gets all the 100 songs from a given date
songs = [item.getText().strip() for item in soup.select("li ul li h3")]
# print(songs)

# for all songs in the songs list, gets the songs' uris
uri_list = []
for item in songs:
    ans = sp.search(q=item, type="track", limit=1)
    uri_list.append(ans["tracks"]["items"][0]["uri"])

# creates the playlist and adds all the songs into it.
playlist_id = sp.user_playlist_create(user=sp.current_user()["id"], name=date+" Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist_id["id"], items=uri_list)
# print(playlist_id)