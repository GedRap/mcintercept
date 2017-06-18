import argparse
import sys

from mcintercept import main_loop


def main(argv={}):
    try:
        main_loop(argv['interface'], argv['port'])
    except KeyboardInterrupt:
        sys.exit('Interrupted by user')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", type=str, help="network interface to listen to", required=True)
    parser.add_argument("-p", "--port", type=int, help="memcached port", default=11211)
    args = parser.parse_args()

    main(
        {
            "interface": args.interface,
            "port": args.port
        }
    )
