'''
gets playlists for each genre seed available
'''
import spotipy
from optparse import OptionParser
from spotipy.oauth2 import SpotifyClientCredentials
import json
import time
import sys
import matplotlib.pyplot as plt
import spotipy.util as util

SPOTIPY_CLIENT_ID = '7c241d674ee243ab88e80c1d183a3e7e'
SPOTIPY_CLIENT_SECRET = 'de6e84f97a5e4162b854ec92f743c3c5'
SPOTIPY_REDIRECT_URI = 'http://localhost/'

username = 'spotifydummy66@gmail.com'
scope = 'playlist-modify-public'


token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)

sp = spotipy.Spotify(auth=token)
sp.trace=False

# get all genres, get recommendations for each genre, output to file
top = ['pop','hip-hop','edm','r-n-b','rock']
uris = ['spotify:user:idw1dm34y0wlm9sjyi56hl2fq:playlist:1t9GGtdzqrOGa4SorE9M7q',
      'spotify:user:idw1dm34y0wlm9sjyi56hl2fq:playlist:3LR7jjBL7dv6O6qU7UXKNK',
      'spotify:user:idw1dm34y0wlm9sjyi56hl2fq:playlist:35IkzXk53IGDYQNLpECDEg',
      'spotify:user:idw1dm34y0wlm9sjyi56hl2fq:playlist:66meeNXPnRN0AfgMrbPiMM',
      'spotify:user:idw1dm34y0wlm9sjyi56hl2fq:playlist:7bRUUBhHkH2Smv2h0hAyzH']

for g, puri in zip(top, uris):
   if g in ['pop', 'hip-hop', 'edm', 'r-n-b']:
      continue
   tracks = sp.recommendations(seed_genres =[g], limit=100)
   user = puri.split(':')[2]
   pid = puri.split(':')[4]
   for track in tracks['tracks']:
      sp.user_playlist_add_tracks(user, pid, tracks=[track['uri']])
