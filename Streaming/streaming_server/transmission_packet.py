class TransmissionPacket:
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
        return TransmissionPacket(request_type, filename, udp_port, seq)
