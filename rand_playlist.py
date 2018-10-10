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
import numpy as np

SPOTIPY_CLIENT_ID = '4192c5a6adeb4aa3966c78a1e81bfa21'
SPOTIPY_CLIENT_SECRET = '109a60c3fc5e4eefbd894935984f09d3'
SPOTIPY_REDIRECT_URI = 'http://localhost/'

client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False

with open('rand_sample.json', 'rb') as of:
   tracks = json.load(of)

sample = np.random.permutation(len(tracks))[:20]
for i in sample:
   t = sp.track(tracks[i][0])
   print t['name'] + ' by ' + t['artists'][0]['name']

