from flask import Flask, request, redirect
from path_fix import *
import twilio.twiml
from soundcloud_settings import *
from soundcloud_interface import *


app = Flask(__name__)

client = soundcloud.Client(client_id=client_id, \
                           client_secret=client_secret, \
                           username=username, \
                           password=password)

@app.route("/")
def enter():
    return "TextTunes Number: " + str(twilio_number)

@app.route("/request", methods=["GET", "POST"])
def receive_message():
    text = request.values.get("Body", None)
    resp = twilio.twiml.Response()

    try:
        song = process_text(text, playlist_uri, client)
        if song:
            resp.message("Thanks for contributing to the playlist! I've added the song '" + song.title + "'.")
        else:
            resp.message("No songs could be found that match query. :(")
    except Exception as e:
        resp.message(str(e))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
