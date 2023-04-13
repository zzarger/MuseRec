import pandas as pd
from langdetect import detect
import re
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

tracks = pd.read_csv('./result.csv')

user_tracks = pd.read_csv('./out.csv', sep='\t')

track_ids = []

for i, row in user_tracks.iterrows():
    track_ids.append(row['id'])

favorites = tracks[tracks.id.isin(track_ids)]

cluster_nums = list(favorites['type'])
clusters = {}

for num in cluster_nums:
    clusters[num] = cluster_nums.count(num)

user_favorite_cluster = [(k, v) for k, v in sorted(clusters.items(), key=lambda item: item[1])][0][0]
suggestions = tracks[tracks.type == user_favorite_cluster]

to_drop = []

for i, row in suggestions.iterrows():
    songid = str(row['id'])
    try:
        suggestions.at[i, 'name'] = songid
    except:
        to_drop.append(i)

suggestions = suggestions.drop(to_drop)
suggestions['name'].to_csv('recs.csv', sep='\t', encoding='utf-8')
