import spotipy
from optparse import OptionParser
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import json
import time
import sys
import os

SPOTIPY_CLIENT_ID = '7c241d674ee243ab88e80c1d183a3e7e'
SPOTIPY_CLIENT_SECRET = 'de6e84f97a5e4162b854ec92f743c3c5'
SPOTIPY_REDIRECT_URI = 'http://localhost/'

username = 'spotifydummy67@gmail.com'
scope = "user-read-playback-state"

token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)

sp = spotipy.Spotify(auth=token)
sp.trace=False

if os.path.isfile('history.json'):
   played = json.load(open('history.json'))
else:
   played = []

while(True):
   try:
      track = sp.current_playback()
      if track is None:
         continue
      if track['item'] is None:
         continue
      if track['item']['id'] not in played:
         played.append(track['item']['id'])
         print "Playing " + track['item']['name'] + ' by ' + track['item']['artists'][0]['name']
         with open('history.json', 'wb') as of:
            json.dump(played, of)
      time.sleep(1)
   except spotipy.client.SpotifyException:
      token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)

      sp = spotipy.Spotify(auth=token)
      sp.trace=False

      track = sp.current_playback()
      if track is None:
         continue
      if track['item']['id'] not in played:
         played.append(track['item']['id'])
         print "Playing " + track['item']['name'] + ' by ' + track['item']['artists'][0]['name']
         with open('history.json', 'wb') as of:
            json.dump(played, of)
      time.sleep(5)
