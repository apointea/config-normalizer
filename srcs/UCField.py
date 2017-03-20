import sys

from .UCException import *
from .UCConfig import *
from .validators.UCVFactory import *
from .validators.UCVException import *

class UCField:

    def __init__(self, name, specs):
        self.name = name
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
        for vInst in self.validators:
            self.__validate(vInst, value)
        self.value = value

    def __validate(self, vInst, value):
        try:
            vInst.check(value)
        except Exception as e:
            p = self.conf.VALIDATOR_POLICY
            msg = "in field '%s' - %s" % (self.field, str(e))
            if p == UCConfig.VALIDATOR_STRICT:
                raise UCException(msg)
            elif p == UCConfig.VALIDATOR_WARNING:
                sys.stderr.write(msg + "\n")

    def export(self):
        return (self.value)
