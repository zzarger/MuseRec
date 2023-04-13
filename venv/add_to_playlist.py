import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util

scope = "playlist-modify-public"
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(), auth_manager=SpotifyOAuth(scope=scope))
tracks = pd.read_csv("./recs.csv", delimiter='\t')

for i, row in tracks.iterrows():
    realid = row['name'].split()[-1]
    sp.playlist_add_items("0o3dKg4Q9Q2bBsxkZCc1k9", [realid])
