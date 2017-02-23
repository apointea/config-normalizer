import re
from .UCValidator import UCValidator

class UCRegex(UCValidator):

    def __init__(self, data):
        self.extractStrProp(data, 'default')
        self.extractStrProp(data, 'pattern')


    def check(self, value):
        if not re.match(self.pattern, value):
            raise ValueError("ERROR value `%s` doesn't look like the pattern." % value)
        return value
