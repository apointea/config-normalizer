# @Author: Antoine Pointeau <kalif>
# @Date:   2017-03-27T01:19:54+02:00
# @Email:  web.pointeau@gmail.com
# @Filename: uniformConfig.py
# @Last modified by:   kalif
# @Last modified time: 2017-04-03T23:34:33+02:00

import sys
import yaml

from .UCException import *
from .UCConfig import *
from .UCChain import *

from .UCStructure import *
from .UCValidators import *

class uniformConfig:

    def __init__(self, modelPath=False, configPath=False):
        self.conf = UCConfig()
        self.context = DSContext()
        self.model = False
        if modelPath:
            self.addModel(modelPath)

    def addModel(self, modelPath):
        cnt = { "path": modelPath }
        md = DSModel(self.conf, self.context, cnt)
        if not self.model: # Set first modell
            self.model = md
            return self
        for prop in md.data: # Merge models
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
        if not data:
            return ""
        return yaml.dump(data, default_flow_style=False)

    def export(self, filePath):
        ext = self.extract()
        with open(filePath, 'w') as out:
            out.write(ext)

    def __toChain(self, key):
        if not isinstance(key, UCChain):
            return UCChain(key)
        return key
