import socket
import threading
import pyaudio
import wave

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
        filename = "D:\\Donwloads\\document\\LittleWing.wav"
        setup_packet = "SETUP " + filename + "\n" + str(
            self.get_transmission_seq()) + "\n" + "UDP " + str(self.stream_port)
        self.transmission_socket.send(setup_packet.encode())
        threading.Thread(target=self.open_stream).start()

    def get_transmission_seq(self):
        self.transmission_seq += 1
        return self.transmission_seq - 1

    def open_stream(self):
        p = pyaudio.PyAudio()
        wf = wave.open("D:\\Donwloads\\document\\LittleWing.wav", 'rb')
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
        stream_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        stream_socket.bind(("127.0.0.1", self.stream_port))  # todo change the server address to be dynamic
        data, addr = stream_socket.recvfrom(1024*4)
        self.frame_list.append(data)
        while data != "done".encode():
            data, addr = stream_socket.recvfrom(1024 * 4)
            self.frame_list.append(data)
        print("done")
        stream.write(b"".join(self.frame_list))
        stream.stop_stream()
        stream.close()

        # close PyAudio (5)
        p.terminate()
        stream_socket.close()



def main():
    c = StreamClient()
    c.main_choise()


if __name__ == '__main__':
    main()
