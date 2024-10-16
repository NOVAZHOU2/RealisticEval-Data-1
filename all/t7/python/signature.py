import logging


class Logger:
    def __init__(self, name, level=logging.DEBUG):
        """
        Initializes a new logger instance.

        :param name: Name of the logger, typically __name__ to reference the module name.
        :param level: Logging level, default is DEBUG.
        """

    def log(self, level, message):
        """
        Logs a message with the given level.

        :param level: Logging level for the message (e.g., logging.INFO).
        :param message: Log message.
        """
