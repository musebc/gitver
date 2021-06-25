"""
Provides stdout/stderr output, with optional color output, if supported
"""

import sys
import os


class Terminal(object):
    """
    Provides a way to output text to the stdout or stderr, optionally
    with colors.
    """
    def __init__(self):
        self.is_quiet = False
        self.is_quiet_err = False

    def set_quiet_flags(self, quiet_stdout, quiet_stderr):
        self.is_quiet = quiet_stdout
        self.is_quiet_err = quiet_stderr

    @staticmethod
    def __emit(text, stream):
        stream.write(text + os.linesep)

    def err(self, text):
        """
        Outputs an ERROR message to the stderr
        """
        if not self.is_quiet_err:
            self.__emit("ERROR: " + text, sys.stderr)

    def warn(self, text):
        """
        Outputs a WARNING message to the stderr
        """
        if not self.is_quiet_err:
            self.__emit("WARNING: " + text, sys.stderr)

    def info(self, text):
        """
        Outputs an INFORMATIVE message to the stderr
        """
        if not self.is_quiet_err:
            self.__emit(text, sys.stderr)

    def out(self, text):
        """
        Outputs a message to the stdout
        """
        if not self.is_quiet:
            self.__emit(text, sys.stdout)


term = Terminal()
