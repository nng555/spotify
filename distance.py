'''Read in a playlist, calculate distances between all pairs of tracks in it, output list of distances to json
'''

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import sys
import itertools

SPOTIPY_CLIENT_ID = '4192c5a6adeb4aa3966c78a1e81bfa21'
SPOTIPY_CLIENT_SECRET = '109a60c3fc5e4eefbd894935984f09d3'
SPOTIPY_REDIRECT_URI = 'http://localhost/'

client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False

from scipy.spatial import distance
import numpy as np

track_features = []

def make_array_features(track_index):
    track_array = []
    track = track_features[track_index]
    track_array.append(track['liveness'])
    track_array.append(track['valence'])
    track_array.append(track['energy'])
    track_array.append(track['danceability'])
    track_array.append(track['speechiness'])
    track_array.append(track['instrumentalness'])
    return track_array

def distance_between_two_tracks(track1index, track2index):
    track1array = make_array_features(track1index)
    track2array = make_array_features(track2index)
    dist = distance.euclidean(track1array, track2array)
    return dist

if len(sys.argv) > 1:
    playlist = sys.argv[1]
data = json.load(open(playlist))
track_list = data['tracks']
filename = data['tracks'][0]['name'] + "_playlist_distances.json"

for i in track_list:
    track_features.extend(sp.audio_features(str(i['id'])))

list_of_distances = []

for a, b in itertools.combinations(track_list, 2):
    dist = distance_between_two_tracks(track_list.index(a), track_list.index(b))
    list_of_distances.append(dist)

print ('average euclidean distance      ', np.mean(list_of_distances))

with open(filename, 'w') as outfile:
    print ('outputting file named ')
    print filename
    json.dump(list_of_distances, outfile)
