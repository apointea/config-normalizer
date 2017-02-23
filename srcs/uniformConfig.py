import yaml
from .UCModel import *

class uniformConfig:

    def __init__(self):
        self.container = False

    def loadModel(self, filePath):
        self.container = UCModel(filePath).build()

    #def loadData(self, filePath):

    def export(self, filePath):
        stream = open(filePath, 'w')
        res = self.container.export()
        yaml.dump(res, stream, default_flow_style=False)
