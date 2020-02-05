from audioStream import AudioSteam


class RequestTransmissionPacket:
    SETUP = "SETUP"

    def __init__(self, request_type="", filename="", udp_port="", rtspSeq=""):
        self.request_type = request_type
        self.filename = filename
        self.udp_port = udp_port
        self.rtspSeq = rtspSeq

    def encode(self, data):
        request = data.split('\n')
        request_type = request[0].split(' ')[0]
        seq = request[1]
        filename = ""
        udp_port = ""
        if request_type == self.SETUP:
            filename = request[0].split(' ')[1]
            udp_port = request[2].split(' ')[1]
        return RequestTransmissionPacket(request_type, filename, udp_port, seq)


class ResponseTransmissionPacket:
    def __init__(self, audio_stream):
        """
        :type audio_stream: AudioSteam
        :param audio_stream:
        """
        self.format = audio_stream.format
        self.channels = audio_stream.channels
        self.rate = audio_stream.rate

    def encode(self):
        response = str(self.format) + "\n" + str(self.channels) + "\n" + str(self.rate)
        return response.encode()
