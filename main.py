#! /usr/bin/env python3

import os
import sys
from optparse import OptionParser

from srcs.uniformConfig import *


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
    (options, args) = parser.parse_args()
    if not options.output:
        parser.error("option -o (output-file) is required")
    return options, args


def main():

    opts, args = parseArguments()

    if opts.example:
        example()
    else:
        pass

def example():
    # Create an UC instance directly with a model path
    UC = uniformConfig("example/myModel/layout")
    # Concatenate another model
    UC.addModel('example/myModel/addon')
    # Export result as string
    print(UC.export())



if (__name__ == '__main__'):
    main()
