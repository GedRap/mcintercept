import unittest

from mcintercept import memcached


class MemcachedTestCase(unittest.TestCase):
    def test_extract_memcached_cmd_and_key_valid(self):
        key = memcached.extract_memcached_cmd_and_key("get foo")
        self.assertEquals(key, ("get", "foo"))

    def test_extract_memcached_cmd_and_key_invalid(self):
        key = memcached.extract_memcached_cmd_and_key("foo bar")
        self.assertIsNone(key)


if __name__ == '__main__':
    unittest.main()
