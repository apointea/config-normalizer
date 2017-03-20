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
        self.model = UCModel(modelPath)

    def addModel(self, modelPath):
        md = UCModel(modelPath)
        for prop in md.data:
            if prop in self.model.data:
                raise UCException("addModel failed, duplicate field: '%s'" % prop)
        self.model.data.update(md.data)
        return self

    def fill(self, dataPath):
        if dataPath.endswith('.yml'):
            return self.fillYaml(dataPath)
        raise UCException("unknown format file : '%s'" % dataPath) # TODO better error there

    def fillYaml(self, dataPath):
        iData = yaml.load(open(dataPath, 'r'))
        return self.setRecursive(iData)

    def __parseKey(self, key):
        if len(key) and key[0] == '.':
            key = key[1:]
        key = key.replace('/', '.').replace('-', '.')
        keys = key.split('.')
        return ([x for x in keys if x != ''])

    def get(self, key):
        return self.model.get(self.__parseKey(key))

    def set(self, key, value):
        self.model.set(self.__parseKey(key), value)

    def setRecursive(self, iData, key=""):
        try:
            self.set(key, iData)
        except: # TODO HANDLE ERRORS
            print('error')
        if isinstance(iData, dict):
            for prop in iData:
                self.setRecursive(iData[prop], key + "." + prop)

    def export(self):
        data = self.model.export()
        return yaml.dump(data, default_flow_style=False)

    def exportFile(self, filePath):
        data = self.model.export()
        fd = open(filePath, 'w')
        yaml.dump(data, fd, default_flow_style=False)
