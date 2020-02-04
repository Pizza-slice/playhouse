import socket
from apiServerWorker import ServerWorker


class Server:
    SERVER_PORT = 6453

    def __init__(self):
        self.server_socket = socket.socket()

    def initialize_server_socket(self):
        self.server_socket.bind(("", self.SERVER_PORT))
        self.server_socket.listen(15)

    def accept_new_connection(self):
        client_socket, client_address = self.server_socket.accept()
        return client_socket


def main():
    s = Server()
    s.initialize_server_socket()
    while True:
        ServerWorker(s.accept_new_connection())
        print("connected")


if __name__ == '__main__':
    main()
