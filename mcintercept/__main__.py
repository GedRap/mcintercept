import argparse
import logging
import sys

from mcintercept import main_loop


def main(argv={}):
    try:
        main_loop(argv['interface'], argv['port'], argv['config'])
    except KeyboardInterrupt:
        sys.exit('Interrupted by user')


if __name__ == "__main__":
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    logging_handler = logging.StreamHandler(sys.stdout)
    logging_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s -- %(message)s')
    logging_handler.setFormatter(formatter)
    root_logger.addHandler(logging_handler)

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", type=str, help="network interface to listen to", required=True)
    parser.add_argument("-c", "--config", type=str, help="path to config file", required=True)

    parser.add_argument("-p", "--port", type=int, help="memcached port", default=11211)
    args = parser.parse_args()

    main(
        {
            "interface": args.interface,
            "port": args.port,
            "config": args.config
        }
    )
