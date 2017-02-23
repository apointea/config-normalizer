import os
import yaml

from .data_structure.model import *

class uniformConfig:

    def __init__(self, modelsDir, patternsDir):
        self.modelsDir = modelsDir
        self.patternsDir = patternsDir
        self.container = False

    def loadModel(self, fileName):
        self.container = model(fileName, self.modelsDir).build()

    #def loadData(self, filePath):

    def export(self, filePath):
        stream = open(filePath, 'w')
        res = self.container.export()
        stream.write(yaml.dump(res))
