# @Author: Antoine Pointeau <kalif>
# @Date:   2017-03-27T01:24:11+02:00
# @Email:  web.pointeau@gmail.com
# @Filename: UCSFactory.py
# @Last modified by:   kalif
# @Last modified time: 2017-04-04T00:30:16+02:00

import os

from ..UCException import *

from .DSModel import *
from .DSPattern import *
from .DSField import *

class Factory:

    @staticmethod
    def create(conf, ctx, cnt):
        if isinstance(cnt, dict) and cnt.get('cmd', False):
            cmd = cnt.get('cmd')
            if cmd == 'include':
                return Factory.__include(conf, ctx, cnt)
            elif cmd == 'pattern':
                return Factory.__pattern(conf, ctx, cnt)
            else:
                raise UCException("unknown command: '%s'" % cmd)
        elif isinstance(cnt, list): # Implicit Pattern use cnt as 'data'
            return DSPattern(conf, ctx, { "data": cnt })
        else: # Implicit Field use cnt as 'default'
            return DSField(conf, ctx, cnt)

    @staticmethod
    def __include(conf, ctx, cnt):
        if cnt.get('path', False):
            return DSModel(conf, ctx, cnt)
        raise UCException("include, 'path' param. not found : '%s'" % ctx.fieldName)

    @staticmethod
    def __pattern(conf, ctx, cnt):
        if cnt.get('data', False):
            return DSPattern(conf, ctx, cnt)
        raise UCException("pattern, 'data' param. not found : '%s'" % ctx.fieldName)
