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
        action = 'store', dest = 'model', default = 'layout',
        help = 'Set the configuration model to use (default: layout.yml)',
    )
    parser.add_option(
        '-mdir', metavar = 'PATH',
        action = 'store', dest = 'modelsDir', default = modelsDir,
        help = 'Set the models directory to use (default: ' + modelsDir + ')'
    )
    parser.add_option(
        '-mdir', metavar = 'PATH',
        action = 'store', dest = 'modelsDir', default = modelsDir,
        help = 'Set the models directory to use (default: ' + modelsDir + ')'
    )
    parser.add_option(
        '-i', '--input-file', metavar = 'FILE',
        action = 'append', dest = 'input',
        help = 'Add an input config file to merge with the model (multiple entries allowed)'
    )
    parser.add_option(
        '-o', '--output-file', metavar = 'FILE',
        action = 'store', dest = 'nominal',
        help = 'Set the output file name, if no input-file, it produce the nominal prototype of the model (required)',
    )
    (options, args) = parser.parse_args()
    return options, args

def main():

    opts, args = parseArguments()

    UC = uniformConfig(opts.modelsDir, opts.patternsDir)
    UC.loadModel('layout')

    if (opts.nominal):
        UC.export(opts.nominal)
    else:
        print('no')


if (__name__ == '__main__'):
    main()
