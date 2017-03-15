from .UCException import *
from .validators.UCValidatorFactory import *

class UCField:

    def __init__(self, specs, field, conf):
        self.field = field
        self.conf = conf
        self.validators = []
        if isinstance(specs, dict):
            self.__initValidators(specs)
            self.set(specs.get("default", ""))
        else:
            self.set(specs)

    vProperties = ["v", "validator", "validators"]
    def __initValidators(self, specs):
        for prop in self.vProperties: # GET VALIDATOR SPECS
            if prop in specs:
                vSpecs = specs[prop]
                try:
                    vInsts = UCValidatorFactory.buildArray(vSpecs)
                    self.validators += vInsts
                except Exception as e:
                    raise UCException("in field '%s' - %s" % (self.field, str(e)))

    def get(self, key):
        if len(key):
            raise UCException()
        return self.value

    def set(self, value):
        for vInst in self.validators:
            if not vInst.check(value):
                raise ValueError('TODO handle validator fail')
        self.value = value

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
            self.set([], data['default'])
