import os
import yaml
import copy

from .UCException import *
from .UCCommon import *
from .UCField import *
from .UCPattern import *
from .UCChain import *

class UCModel(UCCommon):

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
            raise UCException("property '%s' not found in '%s'" % (chain.current(), chain.trace()))
        elem = self.data[chain.current()]
        if isinstance(elem, UCModel):
            return elem.get(copy.copy(chain).next())
        else:
            return elem.get()

    def set(self, chain, value):
        if not self.has(chain):
            raise UCException("property '%s' not found in '%s'" % (chain.current(), chain.trace()))
        elem = self.data[chain.current()]
        if isinstance(elem, UCModel):
            return elem.set(copy.copy(chain).next(), value)
        else:
            return elem.set(value)

    def export(self):
        res = {}
        for prop in self.data:
            res[prop] = self.data[prop].export()
        return res

    # --- INTERNAL METHODS --- #

    def __build(self):
        self.data = {}
        for field in self.fileData:
            cnt = self.fileData[field]
            if isinstance(cnt, dict) and cnt.get('cmd', False):
                self.data[field] = self.__commandRouter(cnt, field)
            else:
                self.data[field] = UCField(field, cnt)

    def __commandRouter(self, cnt, field):
        if cnt['cmd'] == 'include':
            return self.__commandInclude(cnt, field)
        elif cnt['cmd'] == 'pattern':
            return self.__commandPattern(cnt, field)
        raise UCException("unknown command: '%s'" % cnt['cmd'])

    def __commandInclude(self, cnt, field):
        if cnt.get('path', False):
            modelPath = os.path.join(self.dirName, cnt['path'])
            return UCModel(modelPath)
        raise UCException("include, path param. not found : '%s'" % field)

    def __commandPattern(self, cnt, field):
        if cnt.get('path', False):
            patternPath = os.path.join(self.dirName, cnt['path'])
            return UCPattern(patternPath)
        raise UCException("pattern, path param. not found : '%s'" % field)
