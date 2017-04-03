# @Author: Antoine Pointeau <kalif>
# @Date:   2017-03-27T01:27:02+02:00
# @Email:  web.pointeau@gmail.com
# @Filename: UCSField.py
# @Last modified by:   kalif
# @Last modified time: 2017-04-03T23:11:38+02:00

from ..UCException import *
from ..UCValidators import *

from .Interface import *
from .Factory import *

class DSField(Interface):

    def initDS(self, cnt):
        self.validators = []
        if isinstance(cnt, dict):
            self.__initValidators(cnt)
            self.value =  cnt.get("default", None)
        else:
            self.value = cnt
        self.default = self.value

    def __initValidators(self, cnt):
        if "validator" in cnt:
            try:
                vInsts = UCValidatorFactory.buildArray(cnt["validator"])
                self.validators += vInsts
            except Exception as e:
                raise UCException("in field - %s" % str(e))

    def get(self): return self.value

    def set(self, value):
        for v in self.validators:
            v.check(value)
        self.value = value

    def extract(self):
        return (self.value)
