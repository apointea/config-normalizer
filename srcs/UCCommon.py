import os

class UCCommon:

    def checkFilePath(self, filePath):
        if os.path.isfile(filePath):
            return (filePath)
        if not filePath.endswith(".yml"):
            return self.checkFilePath(filePath + ".yml")
        raise UCExceptionFileNotFound("File not found : %s." % filePath)
