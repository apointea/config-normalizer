from .UCException import *

class UCChain:

    def __init__(self, key):
        self.cursor = 0
        props = key.replace('-', '.').replace('/', '.').split('.')
        self.path = [v for v in props if v != '']

    def has(self, index):
        if index < 0 or index >= len(self.path):
            return False
        return True

    def next(self):
        if not self.has(self.cursor + 1):
            raise UCException("index out of bound") # TODO Trace error
        self.cursor += 1
        return self


    def current(self):
        if not self.has(self.cursor):
            raise UCException("index out of bound") # TODO Trace error
        return self.path[self.cursor]

    def trace(self):
        res = ""
        i = 0
        while i < len(self.path):
            if i > 0: res += '.'
            res += self.path[i]
            i += 1
        return res

    def add(self, prop):
        self.path.append(prop)
        return self
