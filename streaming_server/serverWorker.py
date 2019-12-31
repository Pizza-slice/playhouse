import socket
import threading
import time
from audioStream import AudioSteam
from transmission_packet import TransmissionPacket


class ServerWorker(threading.Thread):
    client_info = {}
    SETUP = "SETUP"
    PAUSE = "PAUSE"
    PLAY = "PLAY"
    TEARDOWN = "TEARDOWN"
    TIMER = 0.1794
    END_TRANSMISSION = "$$END_TRANSMISSION$$"

    def __init__(self, client_socket, client_address):
        super(ServerWorker, self).__init__()
        self.client_info["client_socket"] = client_socket
        self.client_info["client_address"] = client_address[0]
        self.start()
        self.playing_event = threading.Event()
        self.playing_event.set()
        self.teardown = False

    def run(self):

        while True:
            transmission_packet = TransmissionPacket().encode(self.client_info["client_socket"].recv(1024).decode())
            if transmission_packet.request_type == self.SETUP:
                self.teardown = False
                self.client_info["audioStream"] = AudioSteam(transmission_packet.filename)
                threading.Thread(target=self.send_stream, args=(transmission_packet.udp_port,)).start()
            elif transmission_packet.request_type == self.PAUSE:
                self.playing_event.clear()
            elif transmission_packet.request_type == self.PLAY:
                self.playing_event.set()
            elif transmission_packet.request_type == self.TEARDOWN:
                self.teardown = True

    def send_stream(self, stream_port):
        stream_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_address = (self.client_info["client_address"], int(stream_port))
        sound_data = self.client_info["audioStream"].get_next_frame(chuck=8820)
        stream_socket.sendto(sound_data, client_address)
        time.sleep(self.TIMER)
        while len(sound_data) > 0 and not self.teardown:
            self.playing_event.wait()
            sound_data = self.client_info["audioStream"].get_next_frame()
            stream_socket.sendto(sound_data, client_address)
            time.sleep(self.TIMER)
        #print("done")
        time.sleep(0.1)
        stream_socket.sendto("$$END_TRANSMISSION$$".encode(), client_address)
        stream_socket.close()
        self.client_info["audioStream"].file.close()
