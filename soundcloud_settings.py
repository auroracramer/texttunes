import json

f = open("/home/j/jt/jtcramer/soundcloud.json", "r")
settings = json.loads(f.read())
f.close()

client_id = settings["client_id"]
client_secret = settings["client_secret"]
redirect_uri = settings["redirect_uri"]
username = settings["username"]
password = settings["password"]
playlist_name = settings["playlist_name"]
twilio_number = settings["twilio_number"]
playlist_uri = "/me/playlists/" + playlist_name
