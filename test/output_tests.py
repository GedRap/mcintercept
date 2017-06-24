import os
import unittest

from mcintercept import output


class OutputTestCase(unittest.TestCase):
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
        container = output.OutputContainer.build_from_string(self.default_input)

        self.assertEquals(len(container.output_handlers), 1)
        self.assertIsInstance(container.output_handlers[0], output.StdoutHandler)

    def test_build_from_string_skip_disabled(self):
        config_str = """
            {
                "patterns": [],
                "output": {
                    "stdout": {
                        "enabled": false
                    }
                }
            }
        """
        container = output.OutputContainer.build_from_string(config_str)

        self.assertEquals(len(container.output_handlers), 0)

    def test_build_from_file(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        container = output.OutputContainer.build_from_file(dir_path + "/data/basic_config.json")

        self.assertEquals(len(container.output_handlers), 1)
        self.assertIsInstance(container.output_handlers[0], output.StdoutHandler)


if __name__ == '__main__':
    unittest.main()
