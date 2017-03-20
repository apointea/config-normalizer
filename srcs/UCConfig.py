import yaml

from .UCException import *
from .UCCommon import *

class UCConfig(UCCommon):

    # FILL POLICY OPTIONS
    FILL_IGNORE             = 1     # ignore if too much data
    FILL_WARNING            = 2     # accept but output a warnign in stderr
    FILL_STRICT             = 3     # raise UCException if too much data

    # VALIDATOR POLICY OPTIONS
    VALIDATOR_IGNORE        = 1     # ignore errors
    VALIDATOR_WARNING       = 2     # accept but ouput a warning in stderr
    VALIDATOR_STRICT        = 3     # raise UCException if not match

    FILL_POLICY             = FILL_WARNING
    VALIDATOR_POLICY        = VALIDATOR_STRICT

    CONFIG_PROPERTIES = [
        "FILL_POLICY",
        "VALIDATOR_POLICY"
    ]

    def __init__(self, filePath=False):
        self.filePath = False
        if filePath:
            self.loadFromFile(filePath)

    def has(self, key):
        return key in UCConfig.CONFIG_PROPERTIES

    def set(self, key, value):
        if self.has(key):
            setattr(self, key, value)
        else:
            raise UCException("configuration property not found : '%s'" % key)

    def get(self, key):
        if self.has(key):
            return getattr(self, key)
        raise UCException("configuration property not found : '%s'" % key)

    def loadFromFile(self, filePath):
        filePath = self.openYaml(filePath)
        data = yaml.load(open(self.filePath), 'r')
        for prop in data:
            self.set(prop, data[prop])
