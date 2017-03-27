# @Author: Antoine Pointeau <kalif>
# @Date:   2017-03-27T01:19:54+02:00
# @Email:  web.pointeau@gmail.com
# @Filename: uniformConfig.py
# @Last modified by:   kalif
# @Last modified time: 2017-03-27T02:17:01+02:00

import sys
import yaml

from .UCException import *
from .UCConfig import *
from .UCChain import *

from .UCStructure import *
from .UCValidators import *

class uniformConfig:

    def __init__(self, modelPath, configPath=False):
        self.conf = UCConfig()
        cnt = { "path": modelPath }
        self.model = DSModel(self.conf, DSContext(), cnt)

    def addModel(self, modelPath):
        cnt = { "path": modelPath }
        md = DSModel(self.conf, DSContext(), cnt)
        for prop in md.data:
            if prop in self.model.data:
                raise UCException("addModel failed, duplicate field: '%s'" % prop)
        self.model.data.update(md.data)
        return self

    def fill(self, dataPath):
        if dataPath.endswith('.yml'):
            return self.fillYaml(dataPath)
        raise UCException("unknown format file : '%s'" % dataPath) # TODO better error there

    def fillYaml(self, dataPath):
        loadData = yaml.load(open(dataPath, 'r'))
        return self.setRecursive(loadData)

    def has(self, key):
        chain = self.__toChain(key)
        return self.model.has(chain)

    def get(self, key):
        chain = self.__toChain(key)
        return self.model.get(chain)

    def set(self, key, value):
        chain = self.__toChain(key)
        try:
            self.model.set(chain, value)
        except UCVException as e:
            msg = "in '%s', %s" % (chain.trace(), str(e))
            if self.conf.VALIDATOR_POLICY == UCConfig.POLICY_STRICT:
                raise UCException(msg)
            elif self.conf.VALIDATOR_POLICY == UCConfig.POLICY_WARNING:
                sys.stderr.write("Error: Uniform Config - %s" % msg)
        except UCException as e:
            raise UCException("in '%s', %s" % (chain.trace(), str(e)))
        return self

    def setRecursive(self, values, chain=UCChain('')):
        if isinstance(values, dict):
            for prop in values:
                self.setRecursive(values[prop], chain.add(prop))
        else:
            self.set(chain, values)

    def extract(self):
        data = self.model.extract()
        return yaml.dump(data, default_flow_style=False)

    def export(self, filePath):
        data = self.model.extract()
        fd = open(filePath, 'w')
        yaml.dump(data, fd, default_flow_style=False)

    def __toChain(self, key):
        if not isinstance(key, UCChain):
            return UCChain(key)
        return key
