import unittest

from mcintercept import memcached


class MemcachedTestCase(unittest.TestCase):
    def test_extract_memcached_key_valid(self):
        key = memcached.extract_memcached_key("get foo")
        self.assertEquals(key, "foo")

    def test_extract_memcached_key_invalid(self):
        key = memcached.extract_memcached_key("foo bar")
        self.assertIsNone(key)


if __name__ == '__main__':
    unittest.main()
