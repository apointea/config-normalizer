import re

from .UCVAbastract import UCVAbastract

class UCVIPv4(UCVAbastract):

    pattern = r"(^((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)$)"

    def emsg(self, value):
        return("validator 'IPv4' reject '%s'" % str(value))

    def child_check(self, value):
        if not re.match(UCVIPv4.pattern, value): return False
        return True
