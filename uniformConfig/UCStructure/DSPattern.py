# @Author: Antoine Pointeau <kalif>
# @Date:   2017-03-27T01:26:15+02:00
# @Email:  web.pointeau@gmail.com
# @Filename: UCSPattern.py
# @Last modified by:   kalif
# @Last modified time: 2017-04-04T00:56:44+02:00

from ..UCException import *

from .Interface import *

class DSPattern(Interface):

    def initDS(self, cnt):
        self.data = []
        if isinstance(cnt["data"], list):
            self.min = len(cnt["data"])
            self.max = len(cnt["data"])
            self.default = self.conf.factory.create(self.conf, self.ctx, "")
            for val in cnt["data"]:
                obj = self.conf.factory.create(self.conf, self.ctx, val)
                self.data.append(obj)
        else:
            self.min = int(cnt.get("min", -1))
            self.max = int(cnt.get("max", -1))
            self.default = self.conf.factory.create(self.conf, self.ctx, cnt["data"])
            self.data = []


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

    def extract(self): # TODO handle min max
        res = []
        for obj in self.data:
            res.append(obj.extract())
        return res
