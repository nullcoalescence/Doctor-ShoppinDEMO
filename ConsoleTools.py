"""
Methods for printing fancy text
"""

from Color_Console import *

class Console:
    colors = {
        "black": 0,
        "red": 1
    }

    attributes = {
        "bold": 1,
        "dim": 2
    }

    def __init__(self):
        print("")

    def print(text, attributes, foreground, background):
        print ('%s test %s' % (fg(foreground), bg(background), attr(attributes)))
