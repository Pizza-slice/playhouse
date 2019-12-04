import socket
import threading
import time
from audioStream import AudioSteam
from transmission_packet import TransmissionPacket


class ServerWorker(threading.Thread):
    client_info = {}
    SETUP = "SETUP"

    def __init__(self, client_socket, client_address):
        super(ServerWorker, self).__init__()
        self.client_info["client_socket"] = client_socket
        self.client_info["client_address"] = client_address[0]
        self.start()

    def run(self):
        transmission_packet = TransmissionPacket().encode(self.client_info["client_socket"].recv(1024).decode())
        if transmission_packet.request_type == self.SETUP:
            self.client_info["audioStream"] = AudioSteam(transmission_packet.filename)
            threading.Thread(target=self.send_stream, args=(transmission_packet.udp_port,)).start()

    def send_stream(self, stream_port):
        stream_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_address = ("127.0.0.1", int(stream_port))
        sound_data = self.client_info["audioStream"].get_next_frame()
        stream_socket.sendto(sound_data, client_address)
        time.sleep(0.01)
        while len(sound_data) > 0:
            sound_data = self.client_info["audioStream"].get_next_frame()
            stream_socket.sendto(sound_data, client_address)
            time.sleep(0.01)
            print(sound_data)
        print("done")
        time.sleep(0.1)
        stream_socket.sendto("done".encode(), client_address)
        stream_socket.close()
        self.client_info["audioStream"].file.close()
