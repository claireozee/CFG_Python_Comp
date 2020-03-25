# 1 - select current mood
# 2 - based on input, pick what you want to feel / we suggest playlists to change that mood
# 3 - results
# 4 - option to play individual songs
# 5 - option to select a particular artist or song if not satisfied
# 6 - extra: create your own playlist from suggested songs

from flask import Flask, render_template, request
from dotenv import load_dotenv
import requests, os
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask("SongSite")

@app.route("/", methods=["GET", "POST"])
def home_page():
#    form_data = request.form
#    currentmood = form_data["currentmood"]
#    wanttofeel = form_data["wanttofeel"]
#   results = suggested_playlist()
    return render_template("index.html")#, currentmood=currentmood, wanttofeel=wanttofeel, results=results)

#def suggested_playlist():
    #"logging in" where else can i put this in terms of entire structure?
#    load_dotenv()
#    api_key = os.getenv("SPOTIFY_TOKEN")
#    api_secret = os.getenv("SPOTIFY_SECRET")
#    client_credentials_manager = SpotifyClientCredentials(api_key, api_secret)
#    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
#    results = spotify.playlist_name_description(name='name', album_type='album', artists='artists')
#    print results
#    return results['items'][4]['name']

app.run(debug=True)
#def
#endpoint 
#url = 'https://api.spotify.com/v1/browse/categories/{category_id}/playlists'

#r = requests.get(url)
#print (r.text)











