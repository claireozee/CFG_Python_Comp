from flask import Flask, render_template, request
from dotenv import load_dotenv
import requests, os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask("MyExampleApp")

@app.route("/")
def home_page():
	return render_template("index.html")

@app.route("/apipage")
def song_page():
	return render_template("apipage.html")

@app.route("/contactus")
def contact_page():
	return render_template("contactus.html")

@app.route("/apiexample", methods=["POST"])
def song():
    #We use the request module to easily collect all the data input into the form
    form_data = request.form
    day = form_data["day"]
    wanttofeel = form_data["wanttofeel"]
    results = birdie()
    #The second argument of the render_template method lets us send data into our html form
    #You can pass multiple things in - just separate them with commas
    #You can also pass in data in lists, and then pull out items from the list within the.html file itself!
    return render_template("apiexample.html", results=results, day=day, wanttofeel=wanttofeel)

def birdie():
    load_dotenv()
    api_key = os.getenv("SPOTIFY_API_KEY")
    api_secret = os.getenv("SPOTIFY_API_SECRET")
    client_credentials_manager = SpotifyClientCredentials(api_key,api_secret)
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
    results = spotify.artist_albums(birdy_uri, album_type='album')
    print results
    return results['items'][4]['name']

def suggestion():
    load_dotenv()
    api_key = os.getenv("SPOTIFY_API_KEY")
    api_secret = os.getenv("SPOTIFY_API_SECRET")
    client_credentials_manager = SpotifyClientCredentials(api_key,api_secret)
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    results = spotify.playlist_name_description(name='name', album_type='album')
    print results
    return results['items'][4]['name']

app.run(debug=True)