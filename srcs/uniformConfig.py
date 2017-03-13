import yaml
from .UCModel import *

class uniformConfig:

    def __init__(self, filePath):
        self.model = UCModel(filePath)

    def __parseKey(self, key):
        return (key.replace('/', '.').replace('-', '.').split('.'))

    def get(self, key):
        return self.model.get(self.__parseKey(key))

    def set(self, key, value):
        self.model.set(self.__parseKey(key), value)

    def export(self, filePath):
        stream = open(filePath, 'w')
        res = self.container.export()
        yaml.dump(res, stream, default_flow_style=False)
