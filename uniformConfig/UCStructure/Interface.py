# @Author: Antoine Pointeau <kalif>
# @Date:   2017-03-27T01:18:44+02:00
# @Email:  web.pointeau@gmail.com
# @Filename: UCSInterface.py
# @Last modified by:   kalif
# @Last modified time: 2017-04-04T00:31:05+02:00

class Interface:

    def __init__(self, conf, ctx, cnt):
        self.conf = conf
        self.ctx = ctx
        self.initDS(cnt)
