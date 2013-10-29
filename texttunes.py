from flask import Flask, request, redirect
from path_fix import *
import twilio.twiml
import soundcloud
from soundcloud_settings import *
from soundcloud_interface import *


app = Flask(__name__)

client = soundcloud.Client(client_id=client_id, \
                           client_secret=client_secret, \
                           username=username, \
                           password=password)

@app.route("/")
def enter():
    print twilio_number
    return "TextTunes number: " + str(twilio_number)

@app.route("/request", methods=["GET", "POST"])
def receive_message():
    text = request.values.get("Body", None)

    process_text(text, playlist_uri, client)

    resp = twilio.twiml.Response()
    resp.message("Thanks for contributing to the playlist! I've added the song '" + song.title + "'.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
