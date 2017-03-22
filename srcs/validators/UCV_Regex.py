import re

from .UCVAbastract import UCVAbastract

class UCVRegex(UCVAbastract):

    def __init__(self, data):
        self.ainit(data)
        if not "pattern" in data:
            raise KeyError("validator 'Regex' no 'pattern' property")
        self.pattern = data.get('pattern')

    def emsg(self, value):
        return("validator 'Regex' reject '%s'" % str(value))

    def child_check(self, value):
        if not re.match(self.pattern, value): return False
        return True
