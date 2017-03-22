import re

from .UCVAbastract import UCVAbastract

class UCVEmail(UCVAbastract):

    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

    def emsg(self, value):
        return("validator 'Email' reject '%s'" % str(value))

    def child_check(self, value):
        if not re.match(UCVEmail.pattern, value): return False
        return True
