import logging

from mcintercept import memcached, network, patterns, output


def main_loop(interface, port, config_file):
    logging.info("Listening to {int} port {port}".format(int=interface, port=port))
    capture = network.Capture(interface, port)

    patterns_container = patterns.PatternsContainer.build_from_file(config_file)
    output_container = output.OutputContainer.build_from_file(config_file)

    logging.info("Loaded config from %s" % config_file)

    for pkt in capture.capture():
        if not isinstance(pkt, str):
            continue

        pkt = pkt.rstrip()
        memcached_data = memcached.extract_memcached_cmd_and_key(pkt)
        if memcached_data is not None:
            memcached_cmd = memcached_data[0]
            memcached_key = memcached_data[1]
            logging.debug("Access to memcached key {key} using {cmd} detected!".format(
                cmd=memcached_cmd, key=memcached_key
            ))

            matching_patterns = patterns_container.find_matching_names(memcached_key)
            if len(matching_patterns) > 0:
                output_container.process(memcached_cmd, memcached_key, matching_patterns)
