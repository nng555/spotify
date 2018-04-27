'''
reads in a playlist, analyzes it
'''

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import sys
import matplotlib.pyplot as plt
import numpy as np

SPOTIPY_CLIENT_ID = '4192c5a6adeb4aa3966c78a1e81bfa21'
SPOTIPY_CLIENT_SECRET = '109a60c3fc5e4eefbd894935984f09d3'
SPOTIPY_REDIRECT_URI = 'http://localhost/'

client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False

if len(sys.argv) > 1:
    playlist = sys.argv[1]
data = json.load(open(playlist))

#get t ids for all tracks
tids = []
for i, c in enumerate(data['tracks']):
    print(' ', i, c['artists'][0]['name'], c['name'])
    tids.append(c['uri'])

#get features for each track
tracks_features = sp.audio_features(tids)

#calculate standard deviations for some values

energies = []
livenesses = []
tempos = []
speechinesses = []
danceabilities = []
loudnesses = []
valences = []
durations = []
keys = []
modes = []
loudnesses = []
instrumentalnesses = []

for i in tracks_features:
    energies.append(i['energy'])
    livenesses.append(i['liveness'])
    tempos.append(i['tempo'])
    speechinesses.append(i['speechiness'])
    danceabilities.append(i['danceability'])
    loudnesses.append(i['loudness'])
    valences.append(i['valence'])
    durations.append(i['duration_ms'])
    keys.append(i['key'])
    modes.append(i['mode'])
    loudnesses.append(i['loudness'])
    instrumentalnesses.append(i['instrumentalness'])

energy_std = np.std(energies)
liveness_std = np.std(livenesses)
speechiness_std = np.std(speechinesses)
danceability_std = np.std(danceabilities)
valences_std = np.std(valences)
loudness_std = np.std(loudnesses)
instrumentalness_std = np.std(instrumentalnesses)

stds = [energy_std, liveness_std, speechiness_std, instrumentalness_std, danceability_std, valences_std]

# get average values over playlist

avg_energy = float(sum(d['energy'] for d in tracks_features) / len(tracks_features))
avg_liveness = float(sum(d['liveness'] for d in tracks_features) / len(tracks_features))
avg_tempo = float(sum(d['tempo'] for d in tracks_features) / len(tracks_features))
avg_speechiness = float(sum(d['speechiness'] for d in tracks_features) / len(tracks_features))
avg_instrumentalness = float(sum(d['instrumentalness'] for d in tracks_features) / len(tracks_features))
avg_danceability = float(sum(d['danceability'] for d in tracks_features) / len(tracks_features))
avg_loudness = float(sum(d['loudness'] for d in tracks_features) / len(tracks_features))
avg_valence = float(sum(d['valence'] for d in tracks_features) / len(tracks_features))
avg_duration = float(sum(d['duration_ms'] for d in tracks_features) / len(tracks_features))

# plot data

averages = (avg_energy, avg_liveness, avg_speechiness, avg_instrumentalness, avg_danceability, avg_valence)
names = ('Energy', "Liveness", "Speechiness", "Instrumentalness", "Danceability", "Valence")

print stds

plt.errorbar(names, averages, stds, linestyle='None', marker='^', capsize=3)
plt.title("Average Values and Std. Dev for Features extracted from playlist " + sys.argv[1])
print ('Standard deviations for energy, liveness, speechiness, instrumentralness, danceability and valence: ' + str(stds))
plt.show()

plt.plot(np.arange(len(tracks_features)), energies)
plt.plot(np.arange(len(tracks_features)), livenesses)
plt.plot(np.arange(len(tracks_features)), speechinesses)
plt.plot(np.arange(len(tracks_features)), valences)

plt.legend(['energy', 'liveness', 'speechiness', 'valence', 'tempo'])
plt.title('Paths taken in recommended tracks')

plt.show()

plt.plot(np.arange(len(tracks_features)), tempos)
plt.title('tempi')
plt.show()
