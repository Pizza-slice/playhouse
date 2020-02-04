import json
import socket
import sys


class Client:
    SERVER_ADDRESS = ("127.0.0.1", 6453)
    SOCKET_BUFFER = 1024

    def __init__(self):
        pass

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

    def recv_response(self, client_socket, repite=False):
        if not repite:
            data = client_socket.recv(self.SOCKET_BUFFER)
            client_socket.close()
            return data
        else:
            data = client_socket.recv(self.SOCKET_BUFFER)
            while len(data) % self.SOCKET_BUFFER == 0:
                data += client_socket.recv(self.SOCKET_BUFFER)
            return data

    def get_album_by_id(self, album_id):
        request = {"endpoint": "info", "type": "album", "album_id": album_id}
        client_socket = self.send_json_request(request)
        response = self.recv_json_response(client_socket)
        return response

    def get_song_by_id(self, song_id):
        request = {"endpoint": "info", "type": "song", "song_id": song_id}
        client_socket = self.send_json_request(request)
        response = self.recv_json_response(client_socket)
        return response

    def get_artist_by_id(self, artist):
        request = {"endpoint": "info", "type": "artist", "artist_id": artist}
        client_socket = self.send_json_request(request)
        response = self.recv_json_response(client_socket)
        return response

    def send_song_query(self, name_of_song):
        request = {"endpoint": "search", "q": name_of_song, "type": "song"}
        client_socket = self.send_json_request(request)
        response = self.recv_json_response(client_socket)
        return response

    def send_artist_query(self, name_of_artist):
        request = {"endpoint": "search", "q": name_of_artist, "type": "artist"}
        client_socket = self.send_json_request(request)
        response = self.recv_json_response(client_socket)
        return response

    def send_album_query(self, name_of_album):
        request = {"endpoint": "search", "q": name_of_album, "type": "album"}
        client_socket = self.send_json_request(request)
        response = self.recv_json_response(client_socket)
        return response

    def send_search_query(self, query):
        request = {"endpoint": "search", "q": query, "type": "all"}
        client_socket = self.send_json_request(request)
        response = self.recv_json_response(client_socket)
        return response

    def send_cover_image_request(self, cover_image_id):
        request = {"endpoint": "coverImage", "q": cover_image_id}
        client_socket = self.send_json_request(request)
        response = self.recv_response(client_socket, repite=True)
        return response


class GuiConnector:
    CACHE_DIR = "cache"

    def __init__(self):
        self.client = Client()
        self.gui_server_socket = socket.socket()
        try:
            self.gui_server_socket.bind(("", int(sys.argv[1])))
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

    def send_json_data(self, massage):
        """
        send data to the gui socket
        :param massage:
        :type massage: dict
        :return:
        """
        self.gui_socket.send(json.dumps(massage).encode())

    def send_data(self, massage):
        self.gui_socket.send(massage)

    def run(self):
        while True:
            request = json.loads(self.recv_data())
            if request["endpoint"] == "search":
                self.handle_search(request)
            elif request["endpoint"] == "album":
                server_response = self.client.get_album_by_id(request["q"])
                self.send_json_data(server_response)
            elif request["endpoint"] == "song":
                server_response = self.client.get_song_by_id(request["q"])
                self.send_json_data(server_response)
            elif request["endpoint"] == "artist":
                server_response = self.client.get_artist_by_id(request["q"])
                self.send_json_data(server_response)
            elif request["endpoint"] == "coverImage":
                server_response = self.client.send_cover_image_request(request["q"])
                with open(self.CACHE_DIR + "\\" + request["q"], "wb+") as f:
                    f.write(server_response)
                print("lol")
                self.send_json_data({"path": self.CACHE_DIR + "\\" + request["q"]})

    def handle_search(self, request):
        if request["type"] == "album":
            server_response = self.client.send_album_query(request["q"])
            self.send_json_data(server_response)
        elif request["type"] == "artist":
            server_response = self.client.send_artist_query(request["q"])
            self.send_json_data(server_response)
        elif request["type"] == "song":
            server_response = self.client.send_song_query(request["q"])
            self.send_json_data(server_response)
        elif request["type"] == "all":
            server_response = self.client.send_search_query(request["q"])
            self.send_json_data(server_response)


if __name__ == "__main__":
    gui_connector = GuiConnector()
    gui_connector.run()
