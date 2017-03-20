from .UCVException import *

class V_Alnum():

    def __init__(self, data):
        pass

    def check(self, value):
        if not str(value).isalnum():
            raise UCVException("validator 'Alnum' reject '%s'" % str(value))
