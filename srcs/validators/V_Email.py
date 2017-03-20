import re

from .UCVException import *

class V_Email():

    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

    def __init__(self, data):
        pass

    def check(self, value):
        if not re.match(UCEmail.pattern, value):
            raise UCVException("validator 'Email' reject '%s'" % str(value))
