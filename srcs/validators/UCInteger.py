from .UCValidator import UCValidator

class UCInteger(UCValidator):

    def __init__(self, data):
        self.extractIntProp(data, 'default')
        self.extractIntProp(data, 'min')
        self.extractIntProp(data, 'max')

    def check(self, value):
        value = int(value)
        if self.min and value < self.min:
            raise ValueError("ERROR value %d < %d(min)" % value, self.min)
        if self.max and value > self.max:
            raise ValueError("ERROR value %d > %d(max)" % value, self.max)
        return value
