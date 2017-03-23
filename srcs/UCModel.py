import os
import yaml
import copy

from .UCException import *
from .UCDataStructure import *
from .UCField import *
from .UCPattern import *
from .UCChain import *

class UCModel(UCDataStructure):

    def __init__(self, modelPath):
        self.filePath = modelPath
        self.dirName = os.path.dirname(self.filePath)
        self.fileData = yaml.load(open(self.filePath, 'r'))
        self.data = {}
        self.__build()

    def has(self, chain):
        if not chain.current() in self.data:
            return False
        return True

    def get(self, chain):
        if not self.has(chain):
            raise UCException("property '%s' not found" % (chain.current(), chain.trace()))
        elem = self.data[chain.current()]
        if isinstance(elem, UCModel):
            return elem.get(copy.copy(chain).next())
        else:
            return elem.get()

    def set(self, chain, value):
        if not self.has(chain):
            raise UCException("property '%s' not found" % (chain.current()))
        elem = self.data[chain.current()]
        if isinstance(elem, UCModel):
            return elem.set(copy.copy(chain).next(), value)
        else:
            return elem.set(value)

    def extract(self):
        res = {}
        for prop in self.data:
            res[prop] = self.data[prop].extract()
        return res

    # --- INTERNAL METHODS --- #

    def __build(self):
        self.data = {}
        for fname in self.fileData:
            cnt = self.fileData[fname]
            self.data[fname] = __buildProp(fname, cnt)
