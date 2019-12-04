import socket
import threading
import wave

import pyaudio


class StreamClient:
    def __init__(self):
        self.transmission_socket = socket.socket()
        self.transmission_socket.connect(("127.0.0.1", 1902))
        self.transmission_seq = 0
        self.stream_port = 4501
        self.lock = threading.Lock()
        self.frame_list = []
        self.done = False

    def main_choise(self):
        # self.send_setup_packet()
        self.send_setup_packet()

    def send_setup_packet(self):
        filename = "C:\\Users\\User\\Downloads\\LittleWing.wav"
        setup_packet = "SETUP " + filename + "\n" + str(
            self.get_transmission_seq()) + "\n" + "UDP " + str(self.stream_port)
        self.transmission_socket.send(setup_packet.encode())
        threading.Thread(target=self.open_stream).start()

    def get_transmission_seq(self):
        self.transmission_seq += 1
        return self.transmission_seq - 1

    def open_stream(self):
        stream_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        stream_socket.bind(("127.0.0.1", self.stream_port))  # todo change the server address to be dynamic
        threading.Thread(target=self.play_stream).start()
        data, addr = stream_socket.recvfrom(8800 * 4)
        self.lock.acquire()
        self.frame_list.append(data)
        self.lock.release()
        while data != "done".encode():
            data, addr = stream_socket.recvfrom(8800 * 4)
            self.lock.acquire()
            self.frame_list.append(data)
            self.lock.release()
        stream_socket.close()

    def play_stream(self):
        p = pyaudio.PyAudio()
        wf = wave.open("C:\\Users\\User\\Downloads\\LittleWing.wav", 'rb')
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
        while True:
            self.lock.acquire()
            frame_list_length = len(self.frame_list)
            self.lock.release()
            for i in range(frame_list_length):
                self.lock.acquire()
                stream.write(self.frame_list.pop(0))
                self.lock.release()

def main():
    c = StreamClient()
    c.main_choise()


if __name__ == '__main__':
    main()
