# @Author: Antoine Pointeau <kalif>
# @Date:   2017-03-27T01:24:24+02:00
# @Email:  web.pointeau@gmail.com
# @Filename: UCSModel.py
# @Last modified by:   kalif
# @Last modified time: 2017-04-03T23:26:39+02:00

import os
import yaml
import copy

from ..UCException import *
from ..UCChain import *

from .Interface import *

class DSModel(Interface):

    def initDS(self, cnt):
        directory = os.path.dirname(self.ctx.path)
        self.file = os.path.join(directory, cnt['path'])
        self.load = yaml.load(open(self.file, 'r'))
        if not self.load: self.load = {}
        self.ctx.path = self.file
        self.data = {}
        for prop in self.load:
            ctx = copy.copy(self.ctx)
            ctx.fieldName = prop
            cnt = self.load[prop]
            self.data[prop] = self.conf.factory.create(self.conf, ctx, cnt)

    def has(self, chain):
        if not chain.current() in self.data:
            return False
        return True

    def get(self, chain):
        if not self.has(chain):
            raise UCException("property '%s' not found" % (chain.current(), chain.trace()))
        elem = self.data[chain.current()]
        if isinstance(elem, DSModel):
            return elem.get(copy.copy(chain).next())
        else:
            return elem.get()

    def set(self, chain, value):
        if not self.has(chain):
            raise UCException("property '%s' not found" % (chain.current()))
        elem = self.data[chain.current()]
        if isinstance(elem, DSModel):
            return elem.set(copy.copy(chain).next(), value)
        else:
            return elem.set(value)

    def extract(self):
        res = {}
        for prop in self.data:
            res[prop] = self.data[prop].extract()
        return res
