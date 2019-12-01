import socket
import pyaudio
import threading
import time

class Client:
    def __init__(self):
        self.transmission_socket = socket.socket()
        self.transmission_socket.connect(("127.0.0.1", 1902))
        self.transmission_seq = 0
        self.stram_port = 4500

    def main_choise(self):
        # self.send_setup_packet()
        self.send_setup_packet()

    def send_setup_packet(self):
        filename = "C:\\Users\\User\Downloads\purple-haze.wav"
        setup_packet = "SETUP " + filename + "\n" + str(
            self.get_transmission_seq()) + "\n" + "UDP " + str(self.stram_port)
        self.transmission_socket.send(setup_packet.encode())
        threading.Thread(target=self.open_stream).start()

    def get_transmission_seq(self):
        self.transmission_seq += 1
        return self.transmission_seq - 1

    def open_stream(self):
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(2),
                        channels=2,
                        rate=48000,
                        output=True)
        stream_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        stream_socket.bind(("127.0.0.1", self.stram_port))  # todo change the server address to be dynamic
        data, addr = stream_socket.recvfrom(1024 * 2 * 2)
        while len(data) > 0:
            stream.write(data)
            time.sleep(0.4)
            data, addr = stream_socket.recvfrom(1024 * 2 * 2)


def main():
    c = Client()
    c.main_choise()


if __name__ == '__main__':
    main()
