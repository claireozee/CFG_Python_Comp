from flask import Flask, render_template, request
from dotenv import load_dotenv
import requests, os
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask("SongSite")

@app.route("/")
def home_page():
	return render_template("index.html")










