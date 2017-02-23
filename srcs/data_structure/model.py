import os
import yaml

from .exception import *
from .field import *

class model:

    def __init__(self, fileName, modelsDir):
        self.fileName = fileName
        self.modelsDir = modelsDir
        stream = self.__openFile()
        self.data = yaml.load(stream)

    def __openFile(self):
        if not self.fileName.endswith('.yml'):
            self.fileName = self.fileName + '.yml'
        filePath = os.path.join(self.modelsDir, self.fileName)
        return open(filePath, 'r')

    def build(self):
        for prop in self.data:
            if isinstance(self.data[prop], str):
                self.data[prop] = field(value=self.data[prop])
            elif isinstance(self.data[prop], dict):
                self.data[prop] = self.__dict(self.data[prop])
            else:
                self.data[prop] = field()
        return (self)

    def export(self):
        res = {}
        for prop in self.data:
            res[prop] = self.data[prop].export()
        return res

    def __dict(self, data):
        if 'command' in data:
            return self.__command(data)
        # Overwise dict is consider as field
        return field('complex')

    def __command(self, data):
        if data['command'] == 'include':
            return self.__include(data)
        elif data['command'] == 'pattern':
            return self.__pattern
        raise ValueError('') # TODO Handle


    def __include(self, data):
        if 'path' in data:
            return model(data['path'].replace('.', '/'), self.modelsDir).build()
        raise UC_ExpectAttrException('IN FILE [' + self.fileName + '] : include command require `path` field')

    def __pattern(self, data):
        raise UC_ExpectAttrException('IN FILE [' + self.fileName + '] : include command require `path` field')
