from mcintercept import memcached
from mcintercept import network


def main_loop(interface, port):
    print "Listening to {int} port {port}".format(int=interface, port=port)
    capture = network.Capture(interface, port)

    for pkt in capture.capture():
        if not isinstance(pkt, str):
            continue

        pkt = pkt.rstrip()
        memcached_data = memcached.extract_memcached_cmd_and_key(pkt)
        if memcached_data is not None:
            print "Access to memcached key {key} using {cmd} detected!".format(
                cmd=memcached_data[0], key=memcached_data[1]
            )
