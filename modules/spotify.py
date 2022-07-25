import os
import time
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def playFile():
    os.system("D:\\led-zeppelin-stairway-to-heaven.mp3")

def playSpotify():
    scope = "user-library-read,user-read-playback-state,user-modify-playback-state"
    client_id='b7b71600f6df4c74a262b890dfae25dd'
    client_secret='b87154d69c264ffda34814da0ad14ac4'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id, client_secret, redirect_uri='http://localhost:8080', scope=scope))

    res = sp.devices()
    pprint(res)

    results = sp.current_user_saved_tracks()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(track['id'], idx, track['artists'][0]['name'], " – ", track['name'])

    sp.shuffle(state=True, device_id='83adcadfec9d82183483a5264de00c6e4b809fe0')

playSpotify()

# while True: time.sleep(0.1)