'''
reads in an track name and a specified number of recommendations, outputs recommended tracks to .json file
'''
import spotipy
import pprint
from optparse import OptionParser
from spotipy.oauth2 import SpotifyClientCredentials
import json
import time
import sys
import matplotlib.pyplot as plt

SPOTIPY_CLIENT_ID = '4192c5a6adeb4aa3966c78a1e81bfa21'
SPOTIPY_CLIENT_SECRET = '109a60c3fc5e4eefbd894935984f09d3'
SPOTIPY_REDIRECT_URI = 'http://localhost/'

client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False

uri = 'spotify:user:spotify:playlist:37i9dQZF1DX5nwnRMcdReF'

results = sp.user_playlist_tracks(uri.split(':')[2], uri.split(':')[4])
tracks = results['items']

pp = pprint.PrettyPrinter(indent=3)

# Loops to ensure I get every track of the playlist
while results['next']:
   results = sp.next(results)
   tracks.extend(results['items'])

genres = {}

i = 0
for track in tracks:
   track_info = track['track']
   #pp.pprint(track_info)
   track_id = track_info['id']
   info = sp.track(track_id)
   artist = sp.artist(info['artists'][0]['uri'])
   for genre in artist['genres']:
      if genre not in genres:
         genres[genre] = 0
      genres[genre] += 1
   i += 1
   if i%1000 == 0:
      print i
      print genres

genrelist = []
for k,v in genres.iteritems():
   genrelist.append([v, k])

print(sorted(genrelist))

