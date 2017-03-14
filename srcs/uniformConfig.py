import yaml

from .UCException import *
from .UCModel import *

class uniformConfig:

    # Policy when fill if the key is not found
    FILL_POLICY_IGNORE   = 0
    FILL_POLICY_ADD      = 1
    FILL_POLICY_ERROR    = 2

    def __init__(self, filePath):
        self.model = UCModel(filePath)

    def joinModel(self, filePath):
        md = UCModel(filePath)
        for prop in md.data:
            if prop in self.model.data:
                raise UCException("joinModel failed, duplicate field: '%s'" % prop)
        self.model.data.update(md.data)

    def fillModel(self, filePath, type, policy=FILL_POLICY_IGNORE):
        pass # TODO

    def __parseKey(self, key):
        return (key.replace('/', '.').replace('-', '.').split('.'))

    def get(self, key):
        return self.model.get(self.__parseKey(key))

    def set(self, key, value):
        self.model.set(self.__parseKey(key), value)


    def export(self, filePath):
        stream = open(filePath, 'w')
        res = self.model.export()
        yaml.dump(res, stream, default_flow_style=False)
