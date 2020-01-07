import socket
import json


class Client:
    SERVER_ADDRESS = ("127.0.0.1", 6453)

    def __init__(self):
        self.client_socket = socket.socket()
        self.connect_socket()

    def connect_socket(self):
        self.client_socket.connect(self.SERVER_ADDRESS)

    def send_json_data(self, request):
        self.client_socket.send(json.dumps(request))

    def recv_json_data(self):
        raw_data = self.client_socket.recv(1024)
        json_data = json.loads(raw_data)
        return json_data

    def get_song_by_id(self, song_id):
        request = {"endpoint": "song", "song_id": song_id}
        self.send_json_data(request)
        json_data = self.recv_json_data()
        return json_data["song"]

    def get_artist_by_id(self, artist):
        request = {"endpoint": "artist", "song_id": artist}
        self.send_json_data(request)
        json_data = self.recv_json_data()
        return json_data["artist"]

    def send_song_query(self, name_of_song):
        request = {"endpoint": "search", "q": name_of_song, "type": "song"}
        self.send_json_data(request)
        json_data = self.recv_json_data()
        return json_data["result"]

    def send_artist_query(self, name_of_artist):
        request = {"endpoint": "search", "q": name_of_artist, "type": "artist"}
        self.send_json_data(request)
        json_data = self.recv_json_data()
        return json_data["result"]

    def send_album_query(self, name_of_album):
        request = {"endpoint": "search", "q": name_of_album, "type": "album"}
        self.send_json_data(request)
        json_data = self.recv_json_data()
        return json_data["result"]


if __name__ == "__main__":
    c = Client()
    result = c.send_album_query("All Things Must Pass")
