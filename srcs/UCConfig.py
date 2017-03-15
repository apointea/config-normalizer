import yaml

from .UCException import *
from .UCCommon import *

class UCConfig(UCCommon):

    # STATIC VALUES         #

    # VALIDATOR POLICY OPTIONS
    VALIDATOR_STRICT       = 1     # raise UCException if not match
    VALIDATOR_INTERPET     = 2     # try interpret the value
    VALIDATOR_WARNING      = 3     # accept but ouput a warning in stderr

    # CONFIG VALUES         #

    # VALIDATOR INSTANCE VALUE
    VALIDATOR_POLICY = VALIDATOR_STRICT

    CONFIG_PROPERTIES = [
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
