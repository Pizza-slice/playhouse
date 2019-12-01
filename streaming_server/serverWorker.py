import threading


class ServerWorker(threading.Thread):
    client_info = {}

    def __init__(self, client_socket):
        super(ServerWorker, self).__init__()
        self.client_info["client_socket"] = client_socket
        self.start()

    def run(self):
        self.client_info["audioStream"]
