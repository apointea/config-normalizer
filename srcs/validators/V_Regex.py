import re

from .UCVException import *

class V_Regex():

    def __init__(self, data):
        if not "pattern" in data:
            raise KeyError("validator 'Regex' no 'pattern' property")
        self.pattern = data.get('pattern')

    def check(self, value):
        if not re.match(self.pattern, value):
            raise UCVException("validator 'Regex' reject '%s'" % str(value))
