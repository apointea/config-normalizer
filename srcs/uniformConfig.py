import yaml
from .UCModel import *

class uniformConfig:

    def __init__(self, filePath):
        self.container = False
        self.container = UCModel(filePath)

    def export(self, filePath):
        stream = open(filePath, 'w')
        res = self.container.export()
        yaml.dump(res, stream, default_flow_style=False)
