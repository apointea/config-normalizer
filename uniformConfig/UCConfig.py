# @Author: Antoine Pointeau <kalif>
# @Date:   2017-03-27T01:10:21+02:00
# @Email:  web.pointeau@gmail.com
# @Filename: UCContext.py
# @Last modified by:   kalif
# @Last modified time: 2017-04-03T23:11:27+02:00

from .UCException import *
from .UCStructure import DSFactory

class UCConfig:

    POLICY_IGNORE             = 1
    POLICY_WARNING            = 2
    POLICY_STRICT             = 4

    FILL_POLICY             = POLICY_IGNORE
    VALIDATOR_POLICY        = POLICY_STRICT

    CONFIG_PROPERTIES = [
        "FILL_POLICY",
        "VALIDATOR_POLICY"
    ]


    def __init__(self):
        self.factory = DSFactory
        pass
