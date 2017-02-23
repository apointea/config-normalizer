import re
from .UCValidator import UCValidator

class UCEmail(UCValidator):

    def __init__(self, data):
        self.extractStrProp(data, 'default')

    def check(self, value):
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", value):
            raise ValueError("ERROR value `%s` doesn't look like an email pattern." % value)
        return value
