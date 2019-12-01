import socket


class Server:
    SERVER_PORT = 1902

    def __init__(self):
        self.server_socket = socket.socket()
        self.server_socket.bind(("", self.SERVER_PORT))
        self.server_socket.listen(10)

    def accept_new_connection(self):
        client_socket, client_address = self.server_socket.accept()
        return client_address, client_address


def main():
    server = Server()
    client_socket, client_address = server.accept_new_connection()
    ServerWorker()

if __name__ == '__main__':
    main()
