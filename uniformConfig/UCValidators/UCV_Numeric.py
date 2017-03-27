from .UCVAbastract import UCVAbastract

class UCVInteger(UCVAbastract):

    def __init__(self, data):
        self.ainit(data)
        self.min = data.get("min", None)
        self.max = data.get("max", None)

    def emsg(self, value):
        return("validator 'Integer' reject '%s'" % str(value))

    def child_check(self, value):
        try: value = int(value)
        except: return False
        if self.min != None and value < int(self.min):
            return False
        if self.max != None and value > int(self.max): return False
        return True
