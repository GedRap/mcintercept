"""
Memcached protocol specifics
"""

# it excludes commands that don't have key as an argument (e.g. stats)
_memcached_commands = [
    "get", "set", "add", "replace", "append", "prepend", "incr", "decr"
]


def extract_memcached_key(data):
    if data is None:
        return None

    data = data.rstrip()

    if data == "":
        return None

    tokens = data.split(" ")

    if (len(tokens) < 2) or (tokens[0].lower() not in _memcached_commands):
        return None

    return tokens[1]
