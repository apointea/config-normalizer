#! /usr/bin/env python

import os
import sys
from optparse import OptionParser

from srcs.uniformConfig import *
from sbin import *

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
        action = 'append', dest = 'input',
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


def main():

    opts, args = parseArguments()
    UC = False

    if opts.example:
        UC = uniformConfig("example/myModel/layout.yml")
    if opts.interactive:
        i = Interactive(UC)
        i.loop()
    else:
        pass

if (__name__ == '__main__'):
    main()
