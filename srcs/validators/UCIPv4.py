import re
from .UCValidator import UCValidator

class UCIPv4(UCValidator):

    def __init__(self, data):
        self.extractStrProp(data, 'default')

    def check(self, value):
        if not re.match(r"(^((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)$)", value):
            raise ValueError("ERROR value `%s` doesn't look like an IPv4 pattern." % value)
        return value
