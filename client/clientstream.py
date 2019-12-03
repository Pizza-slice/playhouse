import socket
import pyaudio
import threading
import wave


class StreamClient:
    def __init__(self):
        self.transmission_socket = socket.socket()
        self.transmission_socket.connect(("127.0.0.1", 1902))
        self.transmission_seq = 0
        self.stram_port = 4500
        self.lock = threading.Lock()
        self.frame_list = []
        self.done = False

    def main_choise(self):
        # self.send_setup_packet()
        self.send_setup_packet()

    def send_setup_packet(self):
        filename = "C:\\Users\\User\Downloads\\LittleWing.wav"
        setup_packet = "SETUP " + filename + "\n" + str(
            self.get_transmission_seq()) + "\n" + "UDP " + str(self.stram_port)
        self.transmission_socket.send(setup_packet.encode())
        threading.Thread(target=self.open_stream).start()

    def get_transmission_seq(self):
        self.transmission_seq += 1
        return self.transmission_seq - 1

    def open_stream(self):
        stream_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        stream_socket.bind(("127.0.0.1", self.stram_port))  # todo change the server address to be dynamic
        threading.Thread(target=self.read_frame)
        data, addr = stream_socket.recvfrom(1024 * 2 * 2)
        self.frame_list.append(data)
        while data != "done".encode():
            data, addr = stream_socket.recvfrom(1024 * 2 * 2)
            self.frame_list.append(data)

    def read_frame(self):
        p = pyaudio.PyAudio()
        wf = wave.open("C:\\Users\\User\Downloads\\LittleWing.wav", 'rb')
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
        while not self.done:
            for i in range(len(self.frame_list)):
                stream.write(self.frame_list.pop(i))
        while len(self.frame_list) > 0:
            for i in range(len(self.frame_list)):
                stream.write(self.frame_list.pop(i))


def main():
    c = StreamClient()
    c.main_choise()


if __name__ == '__main__':
    main()
