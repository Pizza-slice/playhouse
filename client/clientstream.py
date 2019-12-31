import socket
import threading
import wave

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


    def main_choise(self):
        while True:
            inputa = input("please enter stuff")
            if inputa == "SETUP":
                self.is_pause = False
                self.done = False
                self.teardown = False
                threading.Thread(target=self.send_setup_packet).start()
            elif inputa == "PAUSE" and not self.is_pause:
                threading.Thread(target=self.send_pause_massage).start()
                self.is_pause = True
            elif inputa == "PLAY" and self.is_pause:
                threading.Thread(target=self.send_play_massage).start()
                self.is_pause = False
            elif inputa == "T":
                self.done = True
                self.teardown = True
                threading.Thread(target=self.send_teardown_massage).start()

    def send_play_massage(self):
        play_packet = "PLAY " + "\n" + str(self.get_transmission_seq())
        self.transmission_socket.send(play_packet.encode())

    def send_teardown_massage(self):
        teardown_packet = "TEARDOWN " + "\n" + str(self.get_transmission_seq())
        self.transmission_socket.send(teardown_packet.encode())

    def send_pause_massage(self):
        pause_packet = "PAUSE " + "\n" + str(self.get_transmission_seq())
        self.transmission_socket.send(pause_packet.encode())

    def send_setup_packet(self):
        filename = "..\\files\\my_sweet_lord.wav"
        setup_packet = "SETUP " + filename + "\n" + str(
            self.get_transmission_seq()) + "\n" + "UDP " + str(self.stream_port)
        self.transmission_socket.send(setup_packet.encode())
        threading.Thread(target=self.open_stream).start()

    def get_transmission_seq(self):
        self.transmission_seq += 1
        return self.transmission_seq - 1

    def open_stream(self):
        stream_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        stream_socket.bind((self.SERVER_ADDRESS, self.stream_port))  # todo change the server address to be dynamic
        threading.Thread(target=self.play_stream).start()
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

    def play_stream(self):
        p = pyaudio.PyAudio()
        wf = wave.open("..\\files\\my_sweet_lord.wav", 'rb')
        print(wf.getframerate())
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
        while not self.done:
            if self.frame_list:
                self.lock.acquire()
                stream.write(self.frame_list.pop(0))
                self.lock.release()


def main():
    c = StreamClient()
    c.main_choise()


if __name__ == '__main__':
    main()
