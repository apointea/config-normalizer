import os
import yaml

from .UCException import *
from .UCCommon import *
from .UCField import *
from .UCPattern import *

class UCModel(UCCommon):

    def __init__(self, filePath, config=False):
        self.filePath = self.checkFilePath(filePath)
        self.dirName = os.path.dirname(self.filePath)
        self.data = yaml.load(open(self.filePath, 'r'))
        self.__build()

    def __build(self):
        for prop in self.data:
            if isinstance(self.data[prop], dict) and self.data[prop].get('command', False):
                self.data[prop] = self.__commandRouter(prop)
            else:
                self.data[prop] = UCField(self.data[prop])

    def __commandRouter(self, prop):
        if self.data[prop]['command'] == 'include':
            return self.__commandInclude(prop)
        elif self.data[prop]['command'] == 'pattern':
            return self.__commandPattern(prop)
        raise UCException("unknown command: '%s'" % self.data[prop]['command'])

    def __commandInclude(self, prop):
        if self.data[prop].get('path', False):
            fpath = os.path.join(self.dirName, self.data[prop]['path'])
            return UCModel(fpath, self.data[prop])
        raise UCException("include, path param. not found : '%s'" % prop)

    def __commandPattern(self, prop):
        if self.data[prop].get('path', False):
            fpath = os.path.join(self.dirName, self.data[prop]['path'])
            return UCPattern(fpath, self.data[prop])
        raise UCException("pattern, path param. not found : '%s'" % prop)

    def get(self, key):
        if not len(key):
            raise UCException()
        return self.data[key[0]].get(key[1:])

    def set(self, key, value):
        if not len(key):
            raise UCException()
        self.data[key[0]].set(key[1:], value)

    def export(self):
        res = {}
        for prop in self.data:
            res[prop] = self.data[prop].export()
        return res
