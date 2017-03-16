from .UCAlnum import *
from .UCEmail import *
from .UCInteger import *
from .UCIPv4 import *
from .UCRegex import *

class UCValidatorFactory:

    validatorClasses = {
        "alnum": UCAlnum,
        "email": UCEmail,
        "integer": UCInteger,
        "ipv4": UCIPv4,
        "regex": UCRegex
    }

    @staticmethod
    def instanciate(specs):
        if not isinstance(specs, dict):
            raise TypeError("invalid validator type %s" % type(specs))
        if not "v" in specs:
            raise KeyError("validator has no name")
        name = specs.get("v").lower()
        if not name in UCValidatorFactory.validatorClasses:
            raise AttributeError("unknown validator name '%s'" % name)
        vClass = UCValidatorFactory.validatorClasses[name]
        return vClass(specs)

    @staticmethod
    def buildArray(data):
        if not isinstance(data, list):
            return [UCValidatorFactory.instanciate(data)]
        res = []
        for specs in data:
            res.append(UCValidatorFactory.instanciate(specs))
        return res
