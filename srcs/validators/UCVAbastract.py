from .UCVException import *

class UCVAbastract:

    def __init__(self, data): self.ainit(data)

    def ainit(self, data):
        self.neg = data.get("neg", False)

    def check(self, value):
        if self.neg == self.child_check(value):
            raise UCVException(self.emsg(value))
