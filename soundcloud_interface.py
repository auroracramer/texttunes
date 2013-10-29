from path_fix import *
from python26hack import *
import soundcloud

def process_text(text, playlist_uri, client):
    songs = soundcloud_search(text, client)
    if len(songs) > 0:
        song = songs[0]
        add_to_playlist(song.id, playlist_uri, client)
        return song
    else:
        return None

def soundcloud_search(query, client):
    return client.get("/tracks", q=query)

def add_to_playlist(song_id, playlist_uri, client):
    playlist = client.get(playlist_uri)

    old_songs = list(map(lambda track: {"id":track['id']}, playlist.tracks))
    client.put(playlist.uri, playlist={"tracks" : [{"id":song_id}] + old_songs})
