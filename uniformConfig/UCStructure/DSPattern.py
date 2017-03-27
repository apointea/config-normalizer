# @Author: Antoine Pointeau <kalif>
# @Date:   2017-03-27T01:26:15+02:00
# @Email:  web.pointeau@gmail.com
# @Filename: UCSPattern.py
# @Last modified by:   kalif
# @Last modified time: 2017-03-27T01:52:39+02:00

import os
import yaml

from ..UCException import *

from .Interface import *
from .Factory import *

class DSPattern(Interface):

    def __init__(self, fname, data, dirName, specs={}):
        self.name = fname
        self.dirName = dirName
        self.default = self.__buildProp(0, data)
        self.min = specs.get('min', None)
        self.max = specs.get('max', None)
        # TODO there

    def __buildDefault(self, data):
        pass

    def has(self, chain):
        if not chain.current() in self.data:
            return False
        return True

    def get(self, chain):
        if not self.has(chain):
            raise UCException("property '%s' not found" % (chain.current(), chain.trace()))
        elem = self.data[chain.current()]
        if isinstance(elem, UCModel):
            return elem.get(copy.copy(chain).next())
        else:
            return elem.get()


    def set(self, chain, value):
        pass # TODO
