import os
import yaml

from .UCException import *
from .UCCommon import *
from .UCField import *
from .UCPattern import *

class UCModel(UCCommon):

    def __init__(self, modelPath):
        self.filePath = modelPath
        self.dirName = os.path.dirname(self.filePath)
        self.fileData = yaml.load(open(self.filePath, 'r'))
        self.__build()

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

    def get(self, key):
        if not len(key):
            raise UCException()
        return self.data[key[0]].get(key[1:])

    def set(self, key, value):
        if not len(key):
            raise UCException("invalid path '%s'" % key)
        prop = key[0]
        key = key[1:]
        if not prop in self.data:
            raise UCException("fill, prop not found '%s'" % prop)
        if isinstance(self.data[prop], UCField):
            self.data[prop].set(value)
        elif isinstance(self.data[prop], UCModel):
            self.data[prop].set(key, value)
        else:
            raise UCException('non implemented')

    def export(self):
        res = {}
        for prop in self.data:
            res[prop] = self.data[prop].export()
        return res
