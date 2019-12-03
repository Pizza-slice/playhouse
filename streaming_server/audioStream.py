import wave
import pyaudio


class AudioSteam:
    CHUNK = 1024

    def __init__(self, filename):
        self.file = wave.open(filename)
        self.frame_num = 0

    def get_next_frame(self):
        self.frame_num += 1
        return self.file.readframes(self.CHUNK)

    def get_frames(self):
        return self.file.getnframes()


def main():
    p = pyaudio.PyAudio()
    a = AudioSteam("C:\\Users\\User\Downloads\\who-says.wav")
    stream = p.open(format=p.get_format_from_width(a.file.getsampwidth()),
                    channels=a.file.getnchannels(),
                    rate=a.file.getframerate(),
                    output=True)
    data = a.get_next_frame()
    stream.write(data)
    while len(data) > 0:
        data = a.get_next_frame()
        stream.write(data)


if __name__ == '__main__':
    main()
