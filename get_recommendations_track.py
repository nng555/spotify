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

# get track and no. of recommendations desired from command line
if len(sys.argv) > 1:
    track_name = sys.argv[1]
    number_recommendations = (sys.argv[2])
else:
    track_name = 'autumn leaves'
    number_recommendations = 50
# get track ID from name
results = sp.search(q='track:' + track_name, type='track')
possible_tracks = results['tracks']['items']
tracknum = []
#verify correct track
if len(possible_tracks) > 0:
    print ('possible tracks are:')
    for c,i in enumerate(possible_tracks):
        print (c, i['name'], i['artists'][0]['name'])
    tracknum = input("What track do you want as seed?")
    print('track name is ' + possible_tracks[tracknum]['name'] + ' by ' +  possible_tracks[tracknum]['artists'][0]['name'] + ' and the ID is ' + possible_tracks[tracknum]['id'])
    seed = possible_tracks[tracknum]['id']
    tracks = sp.recommendations(seed_tracks = [seed], limit=number_recommendations) #get recommendations from ID

filename = possible_tracks[tracknum]['name'] + "_seeded_tracks.json"
with open(filename, 'w') as outfile:
    json.dump(tracks, outfile)
