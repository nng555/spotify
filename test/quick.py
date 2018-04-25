import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id='965876ed363d4eb18e6cae5a97f6fb73',
      client_secret='da991a6d414d4c7d864a19e84d3f64ea')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = sp.search(q='weezer', limit=20)
for i, t in enumerate(results['tracks']['items']):
      print ' ', i, t['name']
