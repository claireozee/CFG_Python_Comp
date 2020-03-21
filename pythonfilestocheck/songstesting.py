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
def songs():
    #We use the request module to easily collect all the data input into the form
    form_data = request.form["wanttofeel"]
    #day = form_data["day"]
    #wanttofeel = form_data["wanttofeel"]
    #results = form_data["wanttofeel"]
    #message = form_data.get("message", "enter something here fam")

    for "Happy" in form_data["wanttofeel"]:
        results = "Happy"
        print results
    
    else:
        results = "not happy"
        print results
    #    if "Happy" in form_data["wanttofeel"]:
    #        results = "Happy"
    #        print results

    #elif "Happy" in form_data:
    #    results = "HAPPY"
    #    print ("here are the", results, "songs")
    #elif "Energetic" in form_data:
    #    results = "ENERGETIC"
    #    print ("here are the", results, "songs")
   #elif "Excited" in form_data:
    #    results = "EXCITED"
    #    print ("here are the", results, "songs")
  
    #The second argument of the render_template method lets us send data into our html form
    #You can pass multiple things in - just separate them with commas
    #You can also pass in data in lists, and then pull out items from the list within the.html file itself!
    return render_template("apiexample.html", results=results, day=day, wanttofeel=wanttofeel, message = message)

app.run(debug=True)