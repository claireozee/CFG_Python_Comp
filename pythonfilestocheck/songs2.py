from flask import Flask, render_template, request
from dotenv import load_dotenv
import requests, os
import spotipy
import sys
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

#Logging in
client_credentials_manager = SpotifyClientCredentials('5f9f12710cb54579a896598906e69ed3','67c212ed07004d908df6d4f3eac53ea4')
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
#Pulling tracks in playlist
def write_tracks(text_file, tracks):
    with open(text_file, 'a') as file_out:
        while True:
            for item in tracks['items']:
                if 'track' in item:
                    track = item['track']
                else:
                    track = item
                try:
                    track_url = track['external_urls']['spotify']
                    print(track_url + '\n')
                    #file_out.write(track_url + '\n')
                except KeyError:
                    print(u'Skipping track {0} by {1} (local only?)'.format(
                            track['name'], track['artists'][0]['name']))
         # 1 page = 50 results && check if there are more pages
            if tracks['next']:
                tracks = spotify.next(tracks)
            else:
                break
#Pulling playlist
def write_playlist(username, playlist_id):
    results = spotify.user_playlist(username, playlist_id,
                                    fields='tracks,next,name')
    text_file = u'{0}.txt'.format(results['name'], ok='-_()[]{}')
    print(u'Writing {0} tracks to {1}'.format(
            results['tracks']['total'], text_file))
    tracks = results['tracks']
    write_tracks(text_file, tracks)
#Pullin images
def playlist_image(name):
    if len(sys.argv) > 1:
        name = ' '.join(sys.argv[1:])
    else:
        name = name
    results = spotify.search(q='playlist:' + name, type='playlist')
    items = results['playlists']['items']
    if len(items) > 0:
        playlist = items[0]
        print (playlist['name'], playlist['images'][0]['url'])
# The 4 playlists
print('Happy track songs')
write_playlist('Happy Hits!', '37i9dQZF1DXdPec7aLTmlC')
print('Happy track image')
playlist_image('Happy Hits!')

print('Sad track songs')
write_playlist('Sad Songs', '37i9dQZF1DX7qK8ma5wgG1')
print('Sad track image')
playlist_image('Sad Songs')

print('Energetic track songs')
write_playlist('Pump Up Energetic Playlist', '2rtDMBR85xLa22sn1qfzh2')
print('Energetic track image')
playlist_image('Energetic track')

print('Excited track songs')
write_playlist('Exciting songs', '07g7q4u616XlwzvUYGO7Pg?')
print('Excited track image')
playlist_image('Excited track')
