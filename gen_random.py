import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import glob
import sys
import itertools
import numpy as np

SPOTIPY_CLIENT_ID = '4192c5a6adeb4aa3966c78a1e81bfa21'
SPOTIPY_CLIENT_SECRET = '109a60c3fc5e4eefbd894935984f09d3'
SPOTIPY_REDIRECT_URI = 'http://localhost/'

client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False

ids = {}
rand_sample = []
with open('/usr/share/dict/words') as words:
   for word in words:
      word = word.strip()
      print(word)
      for i in range(5):
         offs = i*100
         res = sp.search(q=word, limit=1, offset=offs)['tracks']['items']
         if len(res) == 0:
            break

         track_id = str(res[0]['id'])
         if track_id in ids:
            continue
         ids[track_id] = 1

         track = sp.audio_features(str(res[0]['id']))[0]
         if track is None:
            continue
         track_array = []
         track_array.append(str(res[0]['id']))
         track_array.append(track['liveness'])
         track_array.append(track['valence'])
         track_array.append(track['energy'])
         track_array.append(track['danceability'])
         track_array.append(track['speechiness'])
         track_array.append(track['instrumentalness'])
         track_array.append(track['tempo'])
         track_array.append(track['loudness'])
         track_array.append(track['duration_ms'])
         #track_array.append(track['popularity'])
         track_array.append(track['acousticness'])
         rand_sample.append(track_array)

with open('rand_sample.json', 'wb') as ofile:
   json.dump(rand_sample, ofile)
