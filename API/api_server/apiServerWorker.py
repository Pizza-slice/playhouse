import json
import os
import socket
import threading


class ServerWorker(threading.Thread):
    SOCKET_BUFFER = 1024
    SONG_DIR = "files_matadata\\song_matadata"
    ARTIST_DIR = "files_matadata\\artist_matadata"
    ALBUM_DIR = "files_matadata\\album_matadata"

    def __init__(self, client_socket):
        """
        :param client_socket:
        :type client_socket: socket.socket
        """
        super(ServerWorker, self).__init__()
        self.client_socket = client_socket
        self.start()

    def run(self):
        request = self.recv_json_request()
        if self.check_data(request):
            if request["endpoint"] == "search":
                self.handle_search(request)
            if request["endpoint"] == "info":
                self.handle_info(request)

    def handle_info(self, request):
        """
        handle the search query
        :param request:
        :type request: dict
        :return:
        """
        if request["type"] == "song":
            self.send_json_response({"song": self.get_song_by_id(request["song_id"])})
        if request["type"] == "artist":
            self.send_json_response({"artist": self.get_artist_by_id(request["artist_id"])})
        if request["type"] == "album":
            self.send_json_response({"album": self.get_album_by_id(request["album_id"])})

    def handle_search(self, request):
        """
        handle the search query
        :param request:
        :type request: dict
        :return:
        """
        if request["type"] == "song":
            song_id_list = self.get_song_id_list_by_name(request["q"])
            self.send_json_response({"song": song_id_list})
        if request["type"] == "artist":
            artist_id_list = self.get_artist_id_list_by_name(request["q"])
            self.send_json_response({"artist": artist_id_list})
        if request["type"] == "album":
            album_id_list = self.get_album_id_list_by_name(request["q"])
            self.send_json_response({"album": album_id_list})
        if request["type"] == "all":
            album_id_list = self.get_album_id_list_by_name(request["q"])
            artist_id_list = self.get_artist_id_list_by_name(request["q"])
            song_id_list = self.get_song_id_list_by_name(request["q"])
            self.send_json_response({"song": song_id_list, "artist": artist_id_list, "album": album_id_list})

    def get_album_by_id(self, album_id):
        if os.path.exists(self.ALBUM_DIR + "\\" + album_id + ".json"):
            with open(self.ALBUM_DIR + "\\" + album_id + ".json") as f:
                return json.loads(f.read())
        else:
            return {"error": "not found", "code": "404"}

    def get_artist_by_id(self, artist_id):
        if os.path.exists(self.ARTIST_DIR + "\\" + artist_id + ".json"):
            with open(self.ARTIST_DIR + "\\" + artist_id + ".json") as f:
                return json.loads(f.read())
        else:
            return {"error": "not found", "code": "404"}

    def get_song_by_id(self, song_id):
        if os.path.exists(self.SONG_DIR + "\\" + song_id + ".json"):
            with open(self.SONG_DIR + "\\" + song_id + ".json") as f:
                return json.loads(f.read())
        else:
            return {"error": "not found", "code": "404"}

    def get_album_id_list_by_name(self, name):
        match_song_list = []
        artist_id_list = os.listdir(self.ALBUM_DIR)
        for album in artist_id_list:
            with open(self.ALBUM_DIR + "\\" + album) as f:
                request = json.load(f)
                if name in request["name"]:
                    match_song_list.append(album.split(".")[0])
        return match_song_list

    def get_artist_id_list_by_name(self, name):
        match_song_list = []
        artist_id_list = os.listdir(self.ARTIST_DIR)
        for artist in artist_id_list:
            with open(self.ARTIST_DIR + "\\" + artist) as f:
                request = json.load(f)
                if name in request["name"]:
                    match_song_list.append(artist.split(".")[0])
        return match_song_list

    def get_song_id_list_by_name(self, name):
        match_song_list = []
        song_id_list = os.listdir(self.SONG_DIR)
        for song in song_id_list:
            with open(self.SONG_DIR + "\\" + song) as f:
                request = json.load(f)
                if name in request["name"]:
                    match_song_list.append(song.split(".")[0])
        return match_song_list

    def send_json_response(self, response):
        """
        take a response and send it as a json format
        :param response:
        :type response: dict 
        :return: 
        """
        self.client_socket.send(json.dumps(response).encode())

    def recv_json_request(self):
        """
        recv a request and encode it as a json and return it
        :return response: dict
        """
        return json.loads(self.client_socket.recv(self.SOCKET_BUFFER))

    @staticmethod
    def check_data(request):
        """

        :param request:
        :type request: dict
        """
        info_types = ["song", "album", "artist"]
        keys = request.keys()
        if "endpoint" in keys:
            if request["endpoint"] == "search":
                return "type" in keys and "q" in keys
            if request["endpoint"] == "info":
                return request["type"] in info_types
