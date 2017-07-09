import base64
import unittest

from mcintercept.network import Capture


class NetworkTestCase(unittest.TestCase):
    def test_something(self):
        loopback_packet_base64 = """
        AgAAAEUQAD0YV0AAQAYAAH8AAAF/AAAB63Iry1nBkLd6w7kygBgx1v4xAAABAQgKMtmS+DLZQDRnZXQgZm9vDQo=
        """
        loopback_packet_base64 = loopback_packet_base64.rstrip()
        loopback_packet = base64.b64decode(loopback_packet_base64)

        c = Capture("foo", 12345)
        self.assertEqual(c.extract_data_from_packet(loopback_packet), "get foo\r\n")


if __name__ == '__main__':
    unittest.main()
