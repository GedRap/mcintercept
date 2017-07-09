import pcap

import dpkt


class Capture(object):
    def __init__(self, interface, port):
        self.interface = interface
        self.port = port

        self.sniffer = None
        self.should_stop = False

    def stop(self):
        self.should_stop = True

    def capture(self):
        if self.sniffer is None:
            self.sniffer = pcap.pcap(name=self.interface, timeout_ms=500)
            self.sniffer.setfilter("tcp dst port %d and (tcp[tcpflags] & tcp-push != 0)" % self.port)

        for capture in self.sniffer:
            if self.should_stop:
                break
            if capture is None:
                continue

            packet_timestamp, packet = capture
            packet_data = self.extract_data_from_packet(packet)

            yield packet_data

    def extract_data_from_packet(self, packet):
        # depending on interface and OS, we have either Ethernet or Loopback packet
        # so we will try both and see which it actually is
        if self._attempt_ethernet(packet) is not None:
            return self._attempt_ethernet(packet)

        if self._attempt_loopback(packet) is not None:
            return self._attempt_loopback(packet)

        return None

    def _attempt_ethernet(self, data):
        # this happens on Ubuntu, including when listening on loopback
        eth = dpkt.ethernet.Ethernet(data)
        if isinstance(eth.data, dpkt.ip.IP):
            return eth.data.data.data
        return None

    def _attempt_loopback(self, data):
        # this happens when listening on loopback on MacOS
        loopback = dpkt.loopback.Loopback(data)
        if isinstance(loopback.data, dpkt.ip.IP):
            return loopback.data.data.data
        return None