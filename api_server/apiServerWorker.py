import threading
import socket
import json
import os


class ServerWorker(threading.Thread):
    SOCKET_BUFFER = 1024
    SONG_DIR = "song_matadata"
    ARTIST_DIR = "artist_matadata"
    ALBUM_DIR = "album_matadata"

    def __init__(self, client_socket):
        """
        :param client_socket:
        :type client_socket: socket.socket
        """
        super(ServerWorker, self).__init__()
        self.client_socket = client_socket
        self.start()

    def run(self):
        request = self.client_socket.recv(self.SOCKET_BUFFER)
        json_data = json.loads(request)
        if self.check_data(json_data):
            if json_data["endpoint"] == "search":
                if json_data["type"] == "song":
                    song_id_list = self.get_song_id_list_by_name(json_data["q"])
                    self.client_socket.send(json.dumps({"result": song_id_list}))
                if json_data["type"] == "artist":
                    artist_id_list = self.get_artist_id_list_by_name(json_data["q"])
                    self.client_socket.send(json.dumps({"result": artist_id_list}))
                if json_data["type"] == "album":
                    album_id_list = self.get_album_id_list_by_name(json_data["q"])
                    self.client_socket.send(json.dumps({"result": album_id_list}))
            if json_data["endpoint"] == "song":
                self.client_socket.send(json.dumps({"song": self.get_song_by_id(json_data["song_id"])}))
            if json_data["endpoint"] == "artist":
                self.client_socket.send(json.dumps({"artist": self.get_artist_by_id(json_data["artist_id"])}))
            if json_data["endpoint"] == "album":
                self.client_socket.send(json.dumps({"album": self.get_artist_by_id(json_data["album_id"])}))

    def get_album_by_id(self, album_id):
        if os.path.exists(self.ARTIST_DIR + "\\" + album_id):
            with open(self.ARTIST_DIR + "\\" + album_id) as f:
                return json.loads(f.read())
        else:
            return {"error": "not found", "code": "404"}

    def get_artist_by_id(self, artist_id):
        if os.path.exists(self.ARTIST_DIR + "\\" + artist_id):
            with open(self.ARTIST_DIR + "\\" + artist_id) as f:
                return json.loads(f.read())
        else:
            return {"error": "not found", "code": "404"}

    def get_song_by_id(self, song_id):
        if os.path.exists(self.ARTIST_DIR + "\\" + song_id):
            with open(self.SONG_DIR + "\\" + song_id) as f:
                return json.dumps(f.read())
        else:
            return {"error": "not found", "code": "404"}

    def get_album_id_list_by_name(self, name):
        match_song_list = []
        artist_id_list = os.listdir(self.ALBUM_DIR)
        for album in artist_id_list:
            with open(self.ARTIST_DIR + "\\" + album) as f:
                json_data = json.load(f)
                if name in json_data["name"]:
                    match_song_list.append(album)
        return match_song_list

    def get_artist_id_list_by_name(self, name):
        match_song_list = []
        artist_id_list = os.listdir(self.ARTIST_DIR)
        for artist in artist_id_list:
            with open(self.ARTIST_DIR + "\\" + artist) as f:
                json_data = json.load(f)
                if name in json_data["name"]:
                    match_song_list.append(artist)
        return match_song_list

    def get_song_id_list_by_name(self, name):
        match_song_list = []
        song_id_list = os.listdir(self.SONG_DIR)
        for song in song_id_list:
            with open(self.SONG_DIR + "\\" + song) as f:
                json_data = json.load(f)
                if name in json_data["name"]:
                    match_song_list.append(song)
        return match_song_list

    @staticmethod
    def check_data(json_data):
        """

        :param json_data:
        :type json_data: dict
        """
        keys = json_data.keys()
        if "endpoint" in keys:
            if json_data["endpoint"] == "search":
                return "type" in keys and "q" in keys
            if json_data["endpoint"] == "song":
                return "song_id" in keys
            if json_data["endpoint"] == "artist":
                return "artist_id" in keys
            if json_data["endpoint"] == "album":
                return "album_id" in keys
