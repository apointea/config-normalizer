import os
import yaml

from .UCField import *
from .exception import *

class UCModel:

    def __init__(self, filePath):
        self.filePath = filePath
        if not self.filePath.endswith('.yml'):
            self.filePath = self.filePath + '.yml'
        self.dirname = os.path.dirname(self.filePath)
        self.data = yaml.load(open(self.filePath, 'r'))

    def build(self):
        for prop in self.data:
            if isinstance(self.data[prop], dict) and 'command' in self.data:
                self.data[prop] = self.__command(self.data[prop])
            else:
                self.data[prop] = UCField(self.data[prop])
        return (self)

    def export(self):
        res = {}
        for prop in self.data:
            res[prop] = self.data[prop].export()
        return res

    def __command(self, data):
        if data['command'] == 'include':
            return self.__include(data)
        elif data['command'] == 'pattern':
            return self.__pattern(data)
        raise ValueError('') # TODO Handle


    def __include(self, data):
        if 'path' in data:
            return model(os.path.join(self.dirname, data['path'])).build()
        raise UC_ExpectAttrException('IN FILE [' + self.filePath + '] : include command require `path` field')

    def __pattern(self, data):
        raise UC_ExpectAttrException('IN FILE [' + self.filePath + '] : include command require `path` field')