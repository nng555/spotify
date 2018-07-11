'''
reads in an track name and a specified number of recommendations, outputs recommended tracks to .json file
'''
import spotipy
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

with open('rand_sample.json', 'rb') as of:
   tracks = json.load(of)

genres = {}

i = 0
for track in tracks:
   track_id = track[0]
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

