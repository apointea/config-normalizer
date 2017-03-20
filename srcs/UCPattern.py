import os
import yaml

from .UCException import *
from .UCCommon import *
from .UCField import *

class UCPattern(UCCommon):

    def __init__(self, filePath, conf):
        self.conf = conf
        self.filePath = filePath
        self.dirName = os.path.dirname(self.filePath)
        self.data = yaml.load(open(self.filePath, 'r'))
