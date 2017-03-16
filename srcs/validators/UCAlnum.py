class UCAlnum():

    def __init__(self, data):
        pass

    def check(self, value):
        if not str(value).isalnum():
            raise AssertionError("validator 'Alnum' reject '%s'" % str(value))
