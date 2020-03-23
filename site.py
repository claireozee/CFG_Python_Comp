# 1 - select current mood
# 2 - based on input, pick what you want to feel / we suggest playlists to change that mood
# 3 - option to play individual songs
# 4 - extra: select your own playlist from suggested songs

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













