import os
import unittest

from mcintercept.patterns import PatternsContainer


class PatternsTestCase(unittest.TestCase):
    def setUp(self):
        self.default_input = """
            {
                "patterns": [
                    {
                        "regexp": "^hello",
                        "name": "hello"
                    },
                    {
                        "regexp": "world[0-9]+$",
                        "name": "world"
                    }
                ],
                "output": {
                    "stdout": {
                        "enabled": true
                    }
                }
            }
        """

    def test_build_from_string(self):
        container = PatternsContainer.build_from_string(self.default_input)

        self.assertEquals(len(container.patterns), 2)
        self.assertEquals(container.patterns[0].name, "hello")
        self.assertEquals(container.patterns[0].regexp.pattern, "^hello")
        self.assertEquals(container.patterns[1].name, "world")
        self.assertEquals(container.patterns[1].regexp.pattern, "world[0-9]+$")

    def test_build_from_file(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        container = PatternsContainer.build_from_file(dir_path + "/data/basic_config.json")

        self.assertEquals(len(container.patterns), 2)
        self.assertEquals(container.patterns[0].name, "hello")
        self.assertEquals(container.patterns[0].regexp.pattern, "^hello")
        self.assertEquals(container.patterns[1].name, "world")
        self.assertEquals(container.patterns[1].regexp.pattern, "world[0-9]+$")

    def test_find_matching_names(self):
        container = PatternsContainer.build_from_string(self.default_input)
        container.add_pattern("foo", "foo")

        self.assertEquals(container.find_matching_names("hello world"), ["hello"])
        self.assertEquals(container.find_matching_names("hello foo"), ["hello", "foo"])
        self.assertEquals(container.find_matching_names("nothing"), [])


if __name__ == '__main__':
    unittest.main()
