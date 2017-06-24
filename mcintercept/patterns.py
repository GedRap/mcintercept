import json
import re
from collections import namedtuple

Pattern = namedtuple('Pattern', ['name', 'regexp'])


class PatternsContainer(object):
    def __init__(self):
        self.patterns = list()

    def add_pattern(self, regexp, name):
        self.patterns.append(Pattern(regexp=re.compile(regexp), name=name))

    def find_matching_names(self, key):
        matches = list()

        for pattern in self.patterns:
            if pattern.regexp.search(key) is not None:
                matches.append(pattern.name)

        return matches

    @staticmethod
    def build_from_file(file_path):
        with open(file_path, "r") as f:
            content = f.read()

        return PatternsContainer.build_from_string(content)

    @staticmethod
    def build_from_string(config_json_str):
        config = json.loads(config_json_str)

        if (config is None) or not isinstance(config["patterns"], list):
            raise AttributeError("No valid patterns found.")

        if len(config["patterns"]) == 0:
            raise AttributeError("Patterns list is empty.")

        patterns = config["patterns"]
        container = PatternsContainer()

        for pattern in patterns:
            if ("regexp" not in pattern) or ("name" not in pattern):
                raise AttributeError("Pattern must contain regexp and name.")

            container.add_pattern(pattern["regexp"], pattern["name"])

        return container
