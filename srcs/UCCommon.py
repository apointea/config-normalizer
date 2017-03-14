import os

from .UCException import *

class UCCommon:

    def checkFilePath(self, filePath):
        if os.path.isfile(filePath):
            return (filePath)
        if not filePath.endswith(".yml"):
            return self.checkFilePath(filePath + ".yml")
        raise UCException("file not found : '%s'" % filePath)
