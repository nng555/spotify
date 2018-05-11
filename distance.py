'''Read in a playlist, calculate distances between all pairs of tracks in it, output list of distances to json
'''

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import glob
import sys
import itertools
from scipy.spatial import distance
import numpy as np
import numpy as np
import matplotlib.pyplot as plt


SPOTIPY_CLIENT_ID = '4192c5a6adeb4aa3966c78a1e81bfa21'
SPOTIPY_CLIENT_SECRET = '109a60c3fc5e4eefbd894935984f09d3'
SPOTIPY_REDIRECT_URI = 'http://localhost/'

client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False


#methods

def make_list_of_features(playlist):
    list_of_features = []
    playlist = playlist['tracks']
    for track in playlist:
        list_of_features.extend(sp.audio_features(str(track['id'])))
    return list_of_features

def track_to_array(track_index, list_of_features):
    track_array = []
    track = list_of_features[track_index]
    track_array.append(track['liveness'])
    track_array.append(track['valence'])
    track_array.append(track['energy'])
    track_array.append(track['danceability'])
    track_array.append(track['speechiness'])
    track_array.append(track['instrumentalness'])
    track_array.append(track['tempo'])
    track_array.append(track['key'])
    track_array.append(track['mode'])
    track_array.append(track['time_signature'])
    track_array.append(track['loudness'])
    track_array.append(track['duration_ms'])
    return track_array

def dist_between_pair(track_array1, track_array2):
    dist = distance.euclidean(track_array1, track_array2)
    return dist

def get_average_dist_playlist(playlist):
    list_of_distances = []
    features = make_list_of_features(playlist)
    for a, b in itertools.combinations(features, 2): # get all the distances between all pairs
        first_track = track_to_array(features.index(a), features)
        second_track = track_to_array(features.index(b), features)
        dist = dist_between_pair(first_track, second_track)
        list_of_distances.append(dist)
    average_dist = np.mean(list_of_distances)
    print ('average euclidean dist for playlist is ', average_dist)
    return average_dist

def get_name_and_dist(playlist, file_name):
    dist = get_average_dist_playlist(playlist)
    name = file_name
    return file_name, dist
#####################################################################

list_of_files = glob.glob('./*.json')
results = []
for file_name in list_of_files[:3]:
    data = json.load(open(file_name))
    print ('getting average distance for playlist ', file_name)
    results.append(get_name_and_dist(data, file_name))

labels, ys = zip(*results)
xs = np.arange(len(labels))
width = .2

fig = plt.figure()
ax = fig.gca()  #get current axes
ax.bar(xs, ys, width, align='center')

#Remove the default x-axis tick numbers and
#use tick numbers of your own choosing:
ax.set_xticks(xs)
#Replace the tick numbers with strings:
ax.set_xticklabels(labels)
#Remove the default y-axis tick numbers and
#use tick numbers of your own choosing:
ax.set_yticks(ys)

plt.savefig('distances.png')
