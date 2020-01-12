import json
import socket
import sys


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
        request = {"endpoint": "info", "type": "album", "album_id": album_id}
        client_socket = self.send_json_request(request)
        response = self.recv_json_response(client_socket)
        return response["album"]

    def get_song_by_id(self, song_id):
        request = {"endpoint": "info", "type": "song", "song_id": song_id}
        client_socket = self.send_json_request(request)
        response = self.recv_json_response(client_socket)
        return response["song"]

    def get_artist_by_id(self, artist):
        request = {"endpoint": "info", "type": "artist", "artist_id": artist}
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


class GuiConnector:
    def __init__(self):
        self.gui_server_socket = socket.socket()
        try:
            self.gui_server_socket.bind(("127.0.0.1", int(sys.argv[1])))
        except IndexError:
            raise ValueError("please enter a port")
        self.gui_server_socket.listen(1)
        self.gui_socket = self.gui_server_socket.accept()[0]

    def recv_data(self):
        """
        get data from the gui socket
        :return:
        """
        return self.gui_socket.recv(1024)

    def send_data(self, massage):
        """
        send data to the gui socket
        :param massage:
        :type massage: str
        :return:
        """
        self.gui_socket.send(massage.encode())


if __name__ == "__main__":
    c = Client()
    gui_connector = GuiConnector()
    print(gui_connector.recv_data())
