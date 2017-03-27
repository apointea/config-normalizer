# @Author: Antoine Pointeau <kalif>
# @Date:   2017-03-27T01:18:44+02:00
# @Email:  web.pointeau@gmail.com
# @Filename: UCSInterface.py
# @Last modified by:   kalif
# @Last modified time: 2017-03-27T02:26:09+02:00

class Interface:

    def __init__(self, conf, ctx, cnt):
        self.conf = conf
        self.ctx = ctx
        self.initDS(cnt)
