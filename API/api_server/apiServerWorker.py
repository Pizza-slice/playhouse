import json
import os
import socket
import threading
import base64

import search_engine


class ServerWorker(threading.Thread):
    SOCKET_BUFFER = 1024
    SONG_DIR = "files_matadata\\song_matadata"
    ARTIST_DIR = "files_matadata\\artist_matadata"
    ALBUM_DIR = "files_matadata\\album_matadata"
    COVER_IMAGE_DIR = "files_matadata\\cover_image"

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
            elif request["endpoint"] == "info":
                self.handle_info(request)
            elif request["endpoint"] == "coverImage":
                data = self.get_cover_image(request["q"])
                self.send_response(data)

    def get_cover_image(self, image_id):
        if os.path.isfile(self.COVER_IMAGE_DIR + "\\" + image_id):
            with open(self.COVER_IMAGE_DIR + "\\" + image_id, "rb") as f:
                return f.read()

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
            search_result = search_engine.SearchEngine(request["q"], self.get_song_id_list(), "song").search()
            self.send_json_response({"song": search_result})
        if request["type"] == "artist":
            search_result = search_engine.SearchEngine(request["q"], self.get_artist_id_list(), "artist").search()
            self.send_json_response({"artist": search_result})
        if request["type"] == "album":
            search_result = search_engine.SearchEngine(request["q"], self.get_album_id_list(), "album").search()
            self.send_json_response({"album": search_result})
        if request["type"] == "all":
            search_album = search_engine.SearchEngine(request["q"], self.get_album_id_list(), "album").search()
            search_artist = search_engine.SearchEngine(request["q"], self.get_artist_id_list(), "artist").search()
            search_song = search_engine.SearchEngine(request["q"], self.get_song_id_list(), "song").search()
            self.send_json_response(
                {"song": search_song, "artist": search_artist, "album": search_album})

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

    def get_album_id_list(self):
        match_song_list = []
        artist_id_list = os.listdir(self.ALBUM_DIR)
        for album in artist_id_list:
            match_song_list.append(album.split(".")[0])
        return match_song_list

    def get_artist_id_list(self):
        match_song_list = []
        artist_id_list = os.listdir(self.ARTIST_DIR)
        for artist in artist_id_list:
            match_song_list.append(artist.split(".")[0])
        return match_song_list

    def get_song_id_list(self):
        match_song_list = []
        song_id_list = os.listdir(self.SONG_DIR)
        for song in song_id_list:
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

    def send_response(self, response):
        self.client_socket.send(response)

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
            elif request["endpoint"] == "info":
                return request["type"] in info_types
            elif request["endpoint"] == "coverImage":
                return "q" in keys
