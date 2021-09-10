import os

import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import networkx as nx
import matplotlib.pyplot as plt


def auth_spotify():
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
    return spotipy.Spotify(client_credentials_manager=client_credentials_manager, language="en")

def add_new_artist(artist_id, df):
    artist_info = spotify.artist(artist_id)

    related_artists      = spotify.artist_related_artists(artist_id)
    related_artist_ids   = [artist["id"] for artist in related_artists["artists"]]
    related_artist_names = [artist["name"] for artist in related_artists["artists"]]

    row = pd.Series([artist_info["id"], artist_info["name"], artist_info["popularity"], artist_info["genres"], related_artist_ids, related_artist_names], index=df.columns)
    df  = df.append(row, ignore_index=True)
    return df


spotify = auth_spotify()

artists_df = pd.DataFrame(columns=["id", "name", "popularity", "genres", "related_artist_ids", "related_artist_names"])
missed_artists = [] # search に失敗したアーティスト

# 最初のアーティストを取得
name_id = {"Sambomaster": "5ydDSP9qSxEOlHWnpbblFB", "FLOW": "3w2HqkKa6upwuXEULtGvnY", "Yonezu": "1snhtMLeb2DYoMOcVbb8iB"}
artists_df = add_new_artist(name_id["Yonezu"], artists_df)

l = len(artists_df["related_artist_names"][0])
# l = 3
for i in range(l):
    ids   = artists_df["related_artist_ids"][i]
    names = artists_df["related_artist_names"][i]
    for id, name in zip(ids, names):
        print(name)
        artists_df = add_new_artist(id, artists_df)


# i = 0
# while i<1365:
#     ids   = artists_df["related_artist_ids"][i]
#     names = artists_df["related_artist_names"][i]
#     for id, name in zip(ids[0:l], names[0:l]):
#         print(name)
#         artists_df = add_new_artist(id, artists_df)
#     i += 1

# names = artists_df["related_artist_names"][0]
# for name in names:
#     artists_df = add_new_artist(name, artists_df)


artists_df = artists_df.drop_duplicates(subset="id")

artists_df.to_csv("artists.csv", index=False)

