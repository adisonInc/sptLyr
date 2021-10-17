import lyricsgenius as genius
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import json
import time

f = open("out.txt","wt")
t = open("title.txt","wt")
f2 = open("out2.txt","wt")

#input genius api token here
api = genius.Genius("")


scope = "user-read-currently-playing"


#input spotify api credentials here
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="",
         client_secret="",
         redirect_uri="",
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
