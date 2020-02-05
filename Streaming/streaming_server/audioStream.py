import wave

import pyaudio


class AudioSteam:
    CHUNK = 8820
    MUSIC_PATH = "..\\music_files"

    def __init__(self, filename):
        p = pyaudio.PyAudio()
        self.file = wave.open(self.MUSIC_PATH+"\\"+filename+".wav")
        self.frame_num = 0
        self.format = p.get_format_from_width(self.file.getsampwidth())
        self.channels = self.file.getnchannels()
        self.rate = self.file.getframerate()

    def get_next_frame(self, chuck=CHUNK):
        self.frame_num += 1
        return self.file.readframes(chuck)

    def get_frames(self):
        return self.file.getnframes()


def main():
    p = pyaudio.PyAudio()
    a = AudioSteam("C:\projects\playhouse\Streaming\music_files\\1asod113.wav")
    print(type(p.get_format_from_width(a.file.getsampwidth())), type(a.file.getnchannels()),
          type(a.file.getframerate()))


if __name__ == '__main__':
    main()
