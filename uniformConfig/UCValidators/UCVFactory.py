from .UCV_Alnum       import *
from .UCV_Email       import *
from .UCV_IP          import *
from .UCV_Numeric     import *
from .UCV_Regex       import *

class UCValidatorFactory:

    validatorClasses = {
        "alnum":        UCVAlnum,
        "email":        UCVEmail,
        "integer":      UCVInteger,
        "ipv4":         UCVIPv4,
        "regex":        UCVRegex
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
