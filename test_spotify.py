import os
import json

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def auth_spotify():
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
    return spotipy.Spotify(client_credentials_manager=client_credentials_manager, language='en')

spotify = auth_spotify()

name_id = {"Sambomaster":"5ydDSP9qSxEOlHWnpbblFB", "FLOW":"3w2HqkKa6upwuXEULtGvnY"}
# 日本語名で取得できない
# artist_info = spotify.search(q='artist:' + name, type='artist')
artist_info = spotify.artist(name_id["Sambomaster"])
# print(json.dumps(artist_info)) # artist

# item = artist_info['artists']['items'][0]
# artist_id = item['id']
artist_id = artist_info['id']

related_artists = spotify.artist_related_artists(artist_id)
print(json.dumps(related_artists)) # related_artists
