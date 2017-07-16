import unittest

from mcintercept import memcached


class MemcachedTestCase(unittest.TestCase):
    def test_extract_memcached_cmd_and_key_valid(self):
        key = memcached.extract_memcached_cmd_and_key("set mkey 0 10 5")
        self.assertEquals(key, ("set", ["mkey"]))

    def test_extract_memcached_cmd_and_key_multiple_keys(self):
        key = memcached.extract_memcached_cmd_and_key("get foo bar")
        self.assertEquals(key, ("get", ["foo", "bar"]))

    def test_extract_memcached_cmd_and_key_invalid_command(self):
        key = memcached.extract_memcached_cmd_and_key("foo bar")
        self.assertIsNone(key)


if __name__ == '__main__':
    unittest.main()
