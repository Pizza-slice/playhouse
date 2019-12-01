import threading
from audioStream import AudioSteam
from transmission_packet import TransmissionPacket
import socket
import time


class ServerWorker(threading.Thread):
    client_info = {}
    SETUP = "SETUP"

    def __init__(self, client_socket, client_address):
        super(ServerWorker, self).__init__()
        self.client_info["client_socket"] = client_socket
        self.client_info["client_address"] = client_address[0]
        self.start()

    def run(self):
        self.client_info["audioStream"] = AudioSteam("C:\\Users\\User\Downloads\purple-haze.wav")
        transmission_packet = TransmissionPacket().encode(self.client_info["client_socket"].recv(1024).decode())
        if transmission_packet.request_type == self.SETUP:
            self.client_info["audioStream"] = AudioSteam(transmission_packet.filename)
            threading.Thread(target=self.send_steam, args=(transmission_packet.udp_port,)).start()

    def send_steam(self, stream_port):
        stream_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_address = (self.client_info["client_address"], int(stream_port))
        sound_data = self.client_info["audioStream"].get_next_frame()
        counter = 1
        while len(sound_data) > 0:
            stream_socket.sendto(sound_data, client_address)
            sound_data = self.client_info["audioStream"].get_next_frame()
            print(counter)
            counter += 1


