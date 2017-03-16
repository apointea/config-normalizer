import yaml

from .UCException import *
from .UCConfig import *
from .UCModel import *

class uniformConfig:

    # Policy when fill if the key is not found
    FILL_POLICY_IGNORE   = 0
    FILL_POLICY_ADD      = 1
    FILL_POLICY_ERROR    = 2

    def __init__(self, modelPath=False, configPath=False):
        self.conf = UCConfig(configPath)
        self.model = UCModel(modelPath, self.conf)

    def addModel(self, modelPath):
        md = UCModel(modelPath, self.conf)
        for prop in md.data:
            if prop in self.model.data:
                raise UCException("addModel failed, duplicate field: '%s'" % prop)
        self.model.data.update(md.data)
        return self

    def fillModel(self, filePath, type, policy=FILL_POLICY_IGNORE):
        pass # TODO

    def __parseKey(self, key):
        return (key.replace('/', '.').replace('-', '.').split('.'))

    def get(self, key):
        return self.model.get(self.__parseKey(key))

    def set(self, key, value):
        self.model.set(self.__parseKey(key), value)

    def export(self):
        data = self.model.export()
        return yaml.dump(data, default_flow_style=False)

    def exportFile(self, filePath):
        data = self.model.export()
        fd = open(filePath, 'w')
        yaml.dump(data, fd, default_flow_style=False)
