from mcintercept import memcached
from mcintercept import network


def main_loop(interface, port):
    print "Listening to {int} port {port}".format(int=interface, port=port)
    capture = network.Capture(interface, port)

    for pkt in capture.capture():
        if not isinstance(pkt, str):
            continue

        pkt = pkt.rstrip()
        memcached_key = memcached.extract_memcached_key(pkt)
        if memcached_key is not None:
            print "Access to memcached key %s detected!" % memcached_key
