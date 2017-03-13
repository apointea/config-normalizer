import os
import yaml

from .UCException import *
from .UCCommon import *
from UCField import *

class UCPattern(UCCommon):

    def __init__(self, filePath, config={}):
        self.filePath = self.checkFilePath(filePath)
        self.dirName = os.path.dirname(self.filePath)
        self.data = yaml.load(open(self.filePath, 'r'))
        self.__config(config)

    def __config(self, config):
        self.min = config.get("min", -1)
        self.max = config.get("max", -1)
