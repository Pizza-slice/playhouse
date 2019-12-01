import wave


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
    a = AudioSteam("C:\\Users\\User\Downloads\\purple-haze.wav")
    print(a.file.getframerate())


if __name__ == '__main__':
    main()
