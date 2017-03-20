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

    if opts.example:
        example()
    elif opts.interactive:
        interactive()
    else:
        pass

def example():
    # Create an UC instance directly with a model path
    UC = uniformConfig("example/myModel/layout.yml")
    # Concatenate another model
    UC.addModel('example/myModel/addon.yml')
    # Fill the model with an yml input
    UC.fill('example/myInputs/data.yml')
    # Export result as string
    print(UC.export())

def interactive():
    UC = uniformConfig("example/myModel/layout.yml")
    UC.addModel('example/myModel/addon.yml')
    cond = True
    while(cond):
        print('> ', end='', flush=True)
        cmd = sys.stdin.readline().strip().split(' ')
        if cmd[0] == 'export':
            print(UC.export())
        elif cmd[0] == 'get':
            print(UC.get(cmd[1]))
        elif cmd[0] == 'set':
            UC.set(cmd[1], cmd[2])
        elif cmd[0] == 'has':
            UC.has(cmd[1])
        elif cmd[0] == 'quit':
            exit(0)

if (__name__ == '__main__'):
    main()
