import re

class UCIPv4():

    pattern = r"(^((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)$)"

    def __init__(self, data):
        pass

    def check(self, value):
        if not re.match(UCIPv4.pattern, value):
            raise AssertionError("validator 'IPv4' reject '%s'" % str(value))
