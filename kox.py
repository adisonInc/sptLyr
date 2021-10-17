import lyricsgenius as genius
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import json
import time

f = open("out.txt","wt")
t = open("title.txt","wt")
f2 = open("out2.txt","wt")
api = genius.Genius("R8-EO1pv0aqQNcbmacYFTW8yoLT_4dRq80J4gbImOum2exASp58pFz5-fEuxytrk")

scope = "user-read-currently-playing"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="642322d2139140cfaaf2055634d6e0f5",
         client_secret="f1d90a9ef4344b189fe00768e862cebb",
         redirect_uri="http://localhost:8888/callback",
         scope="user-read-currently-playing"))

result = sp.current_user_playing_track()
track_name = result['item']['name']
artist= result['item']['artists'][0]['name']
song_name = artist + " " + track_name 
print("//////////////////////////////")
print("//////////////////////////////")
print("//////////////////////////////")
print("//////////////////////////////")
print("//////////////////////////////")
print("//////////////////////////////")
print("//////////////////////////////")
print("//////////////////////////////")
print("//////////////////////////////")
print(song_name)
print("//////////////////////////////")
print("//////////////////////////////")
print("//////////////////////////////")
print("//////////////////////////////")
print("//////////////////////////////")
print("//////////////////////////////")
print("//////////////////////////////")
print("//////////////////////////////")
print("//////////////////////////////")
song = api.search_song(song_name)

lyrics = song.lyrics
half = int(len(lyrics)/2) 
f.write(song.lyrics[:half])
f.close()
t.write(song_name)
t.close()
f2.write(song.lyrics[half:])
f2.close()
