import sys

from .UCException import *
from .validators import *


class UCField(UCDataStructure):

    def __init__(self, fname, specs):
        self.name = fname
        self.validators = []
        if isinstance(specs, dict):
            self.__initValidators(specs)
            self.value = specs.get("default", None)
        else:
            self.value = specs
        self.default = self.value

    def __initValidators(self, specs):
        if "validator" in specs:
            try:
                vInsts = UCValidatorFactory.buildArray(specs["validator"])
                self.validators += vInsts
            except Exception as e:
                raise UCException("in field - %s" % str(e))

    def get(self): return self.value

    def set(self, value):
        for v in self.validators:
            v.check(value)
        self.value = value

    def extract(self):
        return (self.value)
