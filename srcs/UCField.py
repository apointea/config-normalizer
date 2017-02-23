from .validators.UCEmail import *
from .validators.UCInteger import *
from .validators.UCIPv4 import *
from .validators.UCRegex import *

class UCField:

    def __init__(self, data):
        self.value = ''
        self.validator = False
        if isinstance(data, dict):
            self.__initDict(data)
        else:
            self.value = data

    def setValue(self, newValue):
        if self.validator:
            self.value = self.validator.check(newValue)
        self.value = newValue

    def export(self):
        return (self.value)

    def __initDict(self, data):
        if 'validate' in data:
            name = data['validate']
            if name == 'email':
                self.validator = UCEmail(data)
            elif name == 'integer':
                self.validator = UCInteger(data)
            elif name == 'IPv4':
                self.validator = UCIPv4(data)
            elif name == 'regex':
                self.validator = UCRegex(data)

        # SET default value (use validator if set)
        if 'default' in data:
            self.setValue(data['default'])
