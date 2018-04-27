'''
reads in an artist and a specified number of recommendations, outputs recommended tracks to .json file
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

# get artist and no. of recommendations desired from command line
if len(sys.argv) > 1:
    artist_name = sys.argv[1]
    number_recommendations = (sys.argv[2])
else:
    artist_name = 'weezer'
    number_recommendations = 10
# get artist ID from name
results = sp.search(q='artist:' + artist_name, type='artist')
items = results['artists']['items']
if len(items) > 0:
    print('artist name is ' + items[0]['name'] + ' and the ID is ' + items[0]['id'])
    seed = items[0]['id']
    tracks = sp.recommendations(seed_artists = [seed], limit=number_recommendations) #get recommendations from ID

filename = items[0]['name'] + "_seeded_tracks.json"
with open(filename, 'w') as outfile:
    json.dump(tracks, outfile)
