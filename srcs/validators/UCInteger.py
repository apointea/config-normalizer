class UCInteger():

    def __init__(self, data):
        self.min = data.get("min", False)
        self.max = data.get("max", False)

    def check(self, value):
        value = int(value)
        if self.min and value < int(self.min):
            raise AssertionError("validator 'Integer' reject '%d' < %d(min)" % (value, self.min))
        if self.max and value > int(self.max):
            raise AssertionError("validator 'Integer' reject '%d' > %d(max)" % (value, self.max))
