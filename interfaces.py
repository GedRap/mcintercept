import pcap

print "All available interfaces:"
for interface in  pcap.findalldevs():
    print " *  %s" % interface