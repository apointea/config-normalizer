from .V_Alnum       import *
from .V_Email       import *
from .V_IP          import *
from .V_Number      import *
from .V_Regex       import *

class UCValidatorFactory:

    validatorClasses = {
        "alnum":        V_Alnum,
        "email":        V_Email,
        "integer":      V_Integer,
        "ipv4":         V_IPv4,
        "regex":        V_Regex
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
