from scapy.all import*

syn_segment = TCP()
syn_segment = TCP(dport=80, seq=123, flags='S')
syn_segment.show()

