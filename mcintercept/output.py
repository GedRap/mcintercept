import json


class OutputHandler(object):
    def process(self, command, key, matched_patterns):
        raise NotImplementedError()


class StdoutHandler(OutputHandler):
    def process(self, command, key, matched_patterns):
        print "command={cmd}, key={key}, patterns={patterns}".format(
            cmd=command, key=key, patterns=matched_patterns
        )


class OutputContainer(object):
    handlers_map = {
        "stdout": StdoutHandler
    }

    def __init__(self):
        self.output_handlers = list()

    def add_handler(self, name, config):
        if name not in OutputContainer.handlers_map:
            raise AttributeError("Invalid output handler: %s" % name)
        handler_cls = OutputContainer.handlers_map[name]

        config.pop("enabled")
        handler = handler_cls(**config)
        self.output_handlers.append(handler)

    def process(self, command, key, matched_patterns):
        if len(self.output_handlers) == 0:
            raise RuntimeError("No output handlers to process message.")

        for handler in self.output_handlers:  # type: OutputHandler
            handler.process(command, key, matched_patterns)

    @staticmethod
    def build_from_file(config_file_path):
        with open(config_file_path, "r") as f:
            content = f.read()

        return OutputContainer.build_from_string(content)

    @staticmethod
    def build_from_string(config_string):
        config = json.loads(config_string)

        if (config is None) or (not isinstance(config["output"], dict)):
            raise AttributeError("Could not find output configuration.")

        output_config = config["output"]  # type: dict
        if len(output_config.keys()) == 0:
            raise AttributeError("No output methods defined in configuration.")

        container = OutputContainer()

        for method_type, method_config in output_config.iteritems():  # type: str, dict
            if not isinstance(method_config, dict):
                raise AttributeError(
                    "Output configuration should be an object. Invalid output method: %s" % method_type
                )

            is_enabled = method_config.get("enabled", False)
            if not is_enabled:
                continue

            container.add_handler(method_type, method_config)

        return container
