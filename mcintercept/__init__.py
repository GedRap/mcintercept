import network

def main_loop(interface, port):
    print "Listening to {int} port {port}".format(int=interface, port=port)
    capture = network.Capture(interface, port)

    for pkt in capture.capture():
        print pkt
