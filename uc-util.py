#! /usr/bin/env python

# @Author: Antoine Pointeau <kalif>
# @Date:   2017-03-27T01:20:39+02:00
# @Email:  web.pointeau@gmail.com
# @Filename: uc-util.py
# @Last modified by:   kalif
# @Last modified time: 2017-04-04T00:05:42+02:00

import os
import sys
from optparse import OptionParser

import uniformConfig as uc
import sbin

def prepareParser():
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    exampleDir = os.path.join(scriptDir, "example")
    modelsDir = os.path.join(exampleDir, "models")
    patternsDir = os.path.join(exampleDir, "patterns")

    usage = "USAGE: %prog [OPTIONS]"
    parser = OptionParser(usage=usage)
    parser.add_option(
        "-m", "--model", metavar = "FILE", action = "append", default = [],
        help = "[REQUIRED at least 1] Model(s) to use",
    )
    parser.add_option(
        "-i", "--input", metavar = "FILE", action = "append", default = [],
        help = "Add an input config file to merge with the model (multiple entries allowed)"
    )
    parser.add_option(
        "-o", "--output", metavar = "FILE", action = "append", default = [],
        help = "Set the output file name, if no input-file, it produce the nominal prototype of the model (default: out.yml)",
    )
    parser.add_option(
        "--example", action = "store_true",
        help = "run included example"
    )
    parser.add_option(
        "-s", "--shell", action = "store_true",
        help = "Build the model and fill it then run an interactive shell"
    )
    return parser

def build(opts, parser):
    if opts.example or not len(opts.input):
        return uc.uniformConfig("example/myModel/layout.yml")
    for idx, path in enumerate(opts.input):
        if idx == 0:
            UCUtil = uc.uniformConfig(path)
        else:
            UCUtil.addModel(path)
    return UCUtil

def main():
    parser = prepareParser()
    (opts, args) = parser.parse_args()
    UCUtil = build(opts, parser)
    if opts.shell:
        sbin.Interactive(UCUtil).loop()

if (__name__ == "__main__"):
    main()
