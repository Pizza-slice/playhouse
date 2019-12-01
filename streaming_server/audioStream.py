import wave


class AudioSteam:
    CHUNK = 1024

    def __init__(self, filename):
        self.file = wave.open(filename)
        self.frame_num = 0

    def get_next_frame(self):
        return self.file.readframes(self.CHUNK)
