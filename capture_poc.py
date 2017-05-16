import sys
import signal

import dpkt
import pcap

print "All available interfaces:"
for interface in  pcap.findalldevs():
    print " *  %s" % interface

if len(sys.argv) < 2:
    interface = "lo0"
else:
    interface = sys.argv[1]

print "Capturing memcached incoming packets"
print "Interface: %s" % interface

sniffer = pcap.pcap(name=interface, timeout_ms=500)
sniffer.setfilter('tcp dst port 11211 and (tcp[tcpflags] & tcp-push != 0)')

for capture in sniffer:
    if capture is None:
        continue

    ts, pkt = capture
    print "{ts:.6f}".format(ts=ts)
    loopback = dpkt.loopback.Loopback(pkt)
    ip = loopback.data
    tcp = ip.data
    content = tcp.data
    print content
