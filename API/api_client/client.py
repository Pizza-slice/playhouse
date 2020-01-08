import json
import socket


class Client:
    SERVER_ADDRESS = ("127.0.0.1", 6453)
    SOCKET_BUFFER = 1024

    def __init__(self):
        self.gui_socket = socket.socket

    def create_connection(self):
        client_socket = socket.socket()
        client_socket.connect(self.SERVER_ADDRESS)
        return client_socket

    def send_json_request(self, request):
        client_socket = self.create_connection()
        client_socket.send(json.dumps(request).encode())
        return client_socket

    def recv_json_response(self, client_socket):
        data = client_socket.recv(self.SOCKET_BUFFER)

        json_response = json.loads(data)
        client_socket.close()
        return json_response

    def get_album_by_id(self, album_id):
        request = {"endpoint": "album", "album_id": album_id}
        client_socket = self.send_json_request(request)
        response = self.recv_json_response(client_socket)
        return response["album"]

    def get_song_by_id(self, song_id):
        request = {"endpoint": "song", "song_id": song_id}
        client_socket = self.send_json_request(request)
        response = self.recv_json_response(client_socket)
        return response["song"]

    def get_artist_by_id(self, artist):
        request = {"endpoint": "artist", "artist_id": artist}
        client_socket = self.send_json_request(request)
        response = self.recv_json_response(client_socket)
        return response["artist"]

    def send_song_query(self, name_of_song):
        request = {"endpoint": "search", "q": name_of_song, "type": "song"}
        client_socket = self.send_json_request(request)
        response = self.recv_json_response(client_socket)
        return response["result"]

    def send_artist_query(self, name_of_artist):
        request = {"endpoint": "search", "q": name_of_artist, "type": "artist"}
        client_socket = self.send_json_request(request)
        response = self.recv_json_response(client_socket)
        return response["result"]

    def send_album_query(self, name_of_album):
        request = {"endpoint": "search", "q": name_of_album, "type": "album"}
        client_socket = self.send_json_request(request)
        response = self.recv_json_response(client_socket)
        return response["result"]


if __name__ == "__main__":
    c = Client()
    result = c.send_album_query("All Thing Must Pass")
    for album in result:
        this_album = c.get_album_by_id(album)
        print("album", this_album)
        for song in this_album["song_list"]:
            print("song", c.get_song_by_id(song))
        print("artist", c.get_artist_by_id(this_album["artist"]))
