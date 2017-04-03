#! /usr/bin/env python

# @Author: Antoine Pointeau <kalif>
# @Date:   2017-03-27T01:20:39+02:00
# @Email:  web.pointeau@gmail.com
# @Filename: uc-util.py
# @Last modified by:   kalif
# @Last modified time: 2017-04-03T23:17:24+02:00

import os
import sys
from optparse import OptionParser

import uniformConfig as uc
import sbin

def parseArguments():
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    exampleDir = os.path.join(scriptDir, 'example')
    modelsDir = os.path.join(exampleDir, 'models')
    patternsDir = os.path.join(exampleDir, 'patterns')

    usage = "USAGE: %prog [options]"
    parser = OptionParser(usage=usage)
    parser.add_option(
        '-m', '--model', metavar = 'NAME',
        action = 'store', dest = 'model',
        help = 'Set the configuration model to use (default: layout.yml)',
    )
    parser.add_option(
        '-i', '--input-file', metavar = 'FILE',
        action = 'append', dest = 'input', default = [],
        help = 'Add an input config file to merge with the model (multiple entries allowed)'
    )
    parser.add_option(
        '-o', '--output-file', metavar = 'FILE',
        action = 'store', dest = 'output', default = 'out.yml',
        help = 'Set the output file name, if no input-file, it produce the nominal prototype of the model (default: out.yml)',
    )
    parser.add_option(
        '--example', metavar = 'EXAMPLE',
        action = 'store_true', dest = 'example', default = False,
        help = 'run included example'
    )
    parser.add_option(
        '--interactive', metavar = 'INTERACTIVE',
        action = 'store_true', dest = 'interactive', default = False,
        help = 'run model in interactive mode'
    )
    (options, args) = parser.parse_args()
    if not options.output:
        parser.error("option -o (output-file) is required")
    return options, args

def build(opts):
    if opts.example:
        return uc.uniformConfig("example/myModel/layout.yml")
    UCUtil = uc.uniformConfig()
    for path in opts.input:
        UCUtil.addModel(path)
    return UCUtil

def main():

    opts, args = parseArguments()
    UCUtil = build(opts)
    if opts.interactive:
        sbin.Interactive(UCUtil).loop()

if (__name__ == '__main__'):
    main()
