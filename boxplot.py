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
import seaborn as sns

def featurize_playlist(playlist):
   playlist = [sp.audio_features(str(playlist['tracks'][i]['id'])) for i in range(len(playlist['tracks']))]
   feat = []
   for track in playlist:
      track = track[0]
      track_array = []
      track_array.append(track['liveness'])
      track_array.append(track['valence'])
      track_array.append(track['energy'])
      track_array.append(track['danceability'])
      track_array.append(track['speechiness'])
      track_array.append(track['instrumentalness'])
      track_array.append(track['tempo'])
      track_array.append(track['loudness'])
      track_array.append(track['duration_ms'])
      #track_array.append(track['popularity'])
      track_array.append(track['acousticness'])
      feat.append(track_array)
   return np.asarray(feat)

def whiten(feat, means, stds):
   new_feat = []
   for ex in feat:
      new_ex = [0 for i in range(len(ex))]
      for i in range(len(ex)):
         new_ex[i] = (ex[i] - means[i])/stds[i]
      new_feat.append(new_ex)
   return new_feat

def boxplot(playlist, sp):
   data = json.load(open(playlist))
   res = featurize_playlist(data)
   means = json.load(open('./means.json'))
   stds = json.load(open('./stds.json'))
   reso = whiten(res, means, stds)
   labels = ['liveness','valence','energy','danceability','speechiness','instrumentalness','tempo','loudness','duration_ms', 'acousticness']
   sns.set()
   sns.despine()
   sns.set_context('talk')
   sns.set_style('white')
   plt.boxplot(np.asarray(reso))
   plt.ylim(-3, 3)
   plt.plot(range(1, 11), reso[0], 'bo')
   plt.xticks(range(1, 11), labels, rotation=-45)
   plt.tight_layout()
   plt.savefig(playlist + '.png')

if __name__=="__main__":
   SPOTIPY_CLIENT_ID = '4192c5a6adeb4aa3966c78a1e81bfa21'
   SPOTIPY_CLIENT_SECRET = '109a60c3fc5e4eefbd894935984f09d3'
   SPOTIPY_REDIRECT_URI = 'http://localhost/'

   client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
   sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
   sp.trace=False

   if len(sys.argv) > 1:
      playlist = sys.argv[1]
      boxplot(playlist, sp)
   else:
      print("Please provide playlist file to analyze")
