import os

from .UCException import *

class UCCommon:

    def openYaml(self, filePath):
        if os.path.isfile(filePath):
            return (filePath)
        if not filePath.endswith(".yml"):
            return self.openYaml(filePath + ".yml")
        raise UCException("file not found : '%s'" % filePath)
