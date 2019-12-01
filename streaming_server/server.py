import socket
from serverWorker import ServerWorker


class Server:
    SERVER_PORT = 1902

    def __init__(self):
        self.transmission_socket = socket.socket()
        self.transmission_socket.bind(("", self.SERVER_PORT))
        self.transmission_socket.listen(10)

    def accept_new_connection(self):
        client_socket, client_address = self.transmission_socket.accept()
        return client_socket, client_address


def main():
    server = Server()
    client_socket, client_address = server.accept_new_connection()
    ServerWorker(client_socket, client_address)


if __name__ == '__main__':
    main()
