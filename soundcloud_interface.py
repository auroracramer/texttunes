from path_fix import *
import soundcloud

def process_text(text, playlist_uri, client):
    add_to_playlist(soundcloud_search(text, client).id, playlist_uri, client)

def soundcloud_search(query, client):
    return client.get("/tracks", q=query)[0]

def add_to_playlist(song_id, playlist_uri, client):
    playlist = client.get(playlist_uri)
    old_songs = list(map(lambda track: {"id":track['id']}, playlist.tracks))
    client.put(playlist.uri, playlist={"tracks" : [{"id":song_id}] + old_songs})
