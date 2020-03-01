import socket
import threading

import pyaudio


class StreamClient:
    SERVER_ADDRESS = "127.0.0.1"

    def __init__(self):
        self.transmission_socket = socket.socket()
        self.transmission_socket.connect((self.SERVER_ADDRESS, 1902))
        self.transmission_seq = 0
        self.stream_port = 4501
        self.lock = threading.Lock()
        self.frame_list = []
        self.done = False
        self.teardown = False
        self.is_pause = False
        self.is_playing = False
        self.is_finish_playing = threading.Event()
        self.is_finish_playing.set()
        self.song_list = []

    def main_loop(self):
        threading.Thread(target=self.run).start()

    def run(self):
        while True:
            if len(self.song_list) > 0:
                self.is_finish_playing.wait()
                self.is_pause = False
                self.done = False
                self.teardown = False
                threading.Thread(target=self.send_setup_packet).start()
                self.is_finish_playing.clear()

    def send_play_massage(self):
        play_packet = "PLAY " + "\n" + str(self.get_transmission_seq())
        self.transmission_socket.send(play_packet.encode())
        self.is_pause = False

    def send_teardown_massage(self):
        teardown_packet = "TEARDOWN " + "\n" + str(self.get_transmission_seq())
        self.transmission_socket.send(teardown_packet.encode())
        self.done = True
        self.teardown = True
        self.is_playing = False
        self.is_finish_playing.set()

    def send_pause_massage(self):
        pause_packet = "PAUSE " + "\n" + str(self.get_transmission_seq())
        self.transmission_socket.send(pause_packet.encode())
        self.is_pause = True

    def send_setup_packet(self):
        setup_packet = "SETUP " + self.song_list.pop(0) + "\n" + str(
            self.get_transmission_seq()) + "\n" + "UDP " + str(self.stream_port)
        self.transmission_socket.send(setup_packet.encode())
        raw_response = self.transmission_socket.recv(1024).decode()
        song_format, channels, rate = self.decode_transmission_response(raw_response)
        threading.Thread(target=self.open_stream, args=(song_format, channels, rate)).start()

    def get_transmission_seq(self):
        self.transmission_seq += 1
        return self.transmission_seq - 1

    def open_stream(self, song_format, channels, rate):
        stream_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        stream_socket.bind((self.SERVER_ADDRESS, self.stream_port))  # todo change the server address to be dynamic
        threading.Thread(target=self.play_stream, args=(song_format, channels, rate)).start()
        data, addr = stream_socket.recvfrom(8820 * 4)
        self.lock.acquire()
        self.frame_list.append(data)
        self.lock.release()
        while data != "$$END_TRANSMISSION$$".encode() and not self.teardown:
            data, addr = stream_socket.recvfrom(8820 * 4)
            self.lock.acquire()
            self.frame_list.append(data)
            self.lock.release()
        stream_socket.close()
        self.done = True

    def play_stream(self, song_format, channels, rate):
        p = pyaudio.PyAudio()
        stream = p.open(format=int(song_format),
                        channels=int(channels),
                        rate=int(rate),
                        output=True)
        self.is_playing = True
        while not self.done:
            if self.frame_list:
                self.lock.acquire()
                stream.write(self.frame_list.pop(0))
                self.lock.release()
        self.is_playing = False
        self.is_finish_playing.set()

    @staticmethod
    def decode_transmission_response(raw_response):
        """
        :type raw_response: str
        :param raw_response:
        :return:
        """
        print(raw_response)
        spited_data_data = raw_response.split("\n")
        return spited_data_data[0], spited_data_data[1], spited_data_data[2]


def main():
    c = StreamClient()


if __name__ == '__main__':
    main()
