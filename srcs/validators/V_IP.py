import re

from .UCVException import *

class V_IPv4():

    pattern = r"(^((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)$)"

    def __init__(self, data):
        pass

    def check(self, value):
        if not re.match(UCIPv4.pattern, value):
            raise UCVException("validator 'IPv4' reject '%s'" % str(value))
