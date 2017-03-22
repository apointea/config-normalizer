import sys

from srcs import *

class Interactive:

    def __init__(self, UC):
        self.UC = UC

    def loop(self):
        while(42):
            sys.stdout.write('> ')
            sys.stdin.flush()
            cmd = sys.stdin.readline().strip().split(' ')
            fct = getattr(self, cmd[0], None)
            if callable(fct):
                fct(cmd)
            else:
                print('USAGE:  TDOD')

    def extract(self, cmd):
        if len(cmd) != 1:
            print('usage: extract')
        else:
            print(self.UC.extract())

    def export(self, cmd):
        if len(cmd) != 2:
            print('usage: export <file path>')
        else:
            self.UC.export(cmd[1])

    def get(self, cmd):
        if len(cmd) != 2:
            print ('usage: get <property>')
        else:
            print(self.UC.get(cmd[1]))

    def has(self, cmd):
        if len(cmd) != 2:
            print ('usage: has <property>')
        else:
            print(self.UC.has(cmd[1]))

    def quit(self, cmd):
        exit(0)

    def set(self, cmd):
        if len(cmd) != 3:
            print('usage: set <property> <value>')
        else:
            try:
                self.UC.set(cmd[1], cmd[2])
            except Exception as e:
                print("error: %s" % str(e))
