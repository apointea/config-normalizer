import yaml

from .UCException import *
from .UCCommon import *

class UCConfig(UCCommon):

    POLICY_IGNORE             = 1
    POLICY_WARNING            = 2
    POLICY_STRICT             = 4

    FILL_POLICY             = POLICY_IGNORE
    VALIDATOR_POLICY        = POLICY_STRICT

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
