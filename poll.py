import spotipy
from optparse import OptionParser
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import json
import time
import sys
import os

logins = json.load(open('login.json', 'wb'))
user = 0

SPOTIPY_CLIENT_ID = logins[user][1]
SPOTIPY_CLIENT_SECRET = logins[user][2]
SPOTIPY_REDIRECT_URI = 'http://localhost/'

username = logins[user][0]
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
         time.sleep(30)
         continue
      if track.get('item') is None:
         time.sleep(30)
         continue
      if track['item'].get('id') is None:
         time.sleep(30)
         continue
      if track['item']['id'] not in played:
         played.append(track['item']['id'])
         print "Playing " + track['item']['name'] + ' by ' + track['item']['artists'][0]['name']
         with open('history.json', 'wb') as of:
            json.dump(played, of)
      time.sleep(30)
   except spotipy.client.SpotifyException:
      token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)

      sp = spotipy.Spotify(auth=token)
      sp.trace=False

      track = sp.current_playback()
      if track is None:
         time.sleep(30)
         continue
      if track.get('item') is None:
         time.sleep(30)
         continue
      if track['item'].get('id') is None:
         time.sleep(30)
         continue
      if track['item']['id'] not in played:
         played.append(track['item']['id'])
         print "Playing " + track['item']['name'] + ' by ' + track['item']['artists'][0]['name']
         with open('history.json', 'wb') as of:
            json.dump(played, of)
      time.sleep(30)
