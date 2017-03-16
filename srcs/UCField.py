import sys

from .UCException import *
from .UCConfig import *
from .validators.UCValidatorFactory import *

class UCField:

    def __init__(self, specs, field, conf):
        self.field = field
        self.conf = conf
        self.validators = []
        if isinstance(specs, dict):
            self.__initValidators(specs)
            self.value = specs.get("default", None)
        else:
            self.value = specs

    def __initValidators(self, specs):
        if "validator" in specs:
            try:
                vInsts = UCValidatorFactory.buildArray(specs["validator"])
                self.validators += vInsts
            except Exception as e:
                raise UCException("in field '%s' - %s" % (self.field, str(e)))

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
