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

SPOTIPY_CLIENT_ID = '4192c5a6adeb4aa3966c78a1e81bfa21'
SPOTIPY_CLIENT_SECRET = '109a60c3fc5e4eefbd894935984f09d3'
SPOTIPY_REDIRECT_URI = 'http://localhost/'

client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False

# get all genres, get recommendations for each genre, output to file
seeds = sp.recommendation_genre_seeds()
print(type(seeds['genres']))
for i in (seeds['genres']):
    tracks = sp.recommendations(seed_genres =[i], limit=100)
    print('outputting playlist for genre ' + i)
    filename = i + "_seeded_tracks.json"
    with open(filename, 'w') as outfile:
        json.dump(tracks, outfile)
