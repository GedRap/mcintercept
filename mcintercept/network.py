import pcap

import dpkt


class Capture(object):
    def __init__(self, interface, port):
        self.interface = interface
        self.port = port

        self.sniffer = pcap.pcap(name=self.interface, timeout_ms=500)
        self.sniffer.setfilter("tcp dst port %d and (tcp[tcpflags] & tcp-push != 0)" % self.port)

        self.should_stop = False

    def stop(self):
        self.should_stop = True

    def capture(self):
        for capture in self.sniffer:
            if capture is None:
                continue

            packet_timestamp, packet = capture
            packet_data = self.extract_data_from_packet(packet)

            yield packet_data

    def extract_data_from_packet(self, packet):
        loopback = dpkt.loopback.Loopback(packet)
        ip = loopback.data
        tcp = ip.data
        content = tcp.data

        return content
