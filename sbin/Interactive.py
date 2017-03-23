import sys
import re

class Interactive:

    prompt = '> '

    def __init__(self, UC):
        self.UC = UC

    def loop(self):
        while(42):
            line = self.getLine()
            cline = self.cleanLine(line)
            cmd = cline.split(' ')
            if cline != '':
                self.runCmd(cmd)

    def getLine(self):
        sys.stdout.write(self.prompt)
        sys.stdout.flush()
        return sys.stdin.readline()

    def cleanLine(self, line):
        line = line.strip()
        line = line.replace(' +', ' ')
        return line

    def runCmd(self, cmd):
        fct = getattr(InteractiveCmd, cmd[0], None)
        if callable(fct):
            fct(self.UC, cmd)
        else:
            print("unknown command type 'help' to see usage")

class InteractiveCmd:

    # --- Utils ---------------------------------------------------------------#
    @staticmethod
    def help(UC, cmd):
        print('Commands :')
        print('\n  --- Utils ---')
        print('    help                   - show this message')
        print('    extract                - print the current model state (usefull for debug)')
        print('    quit                   - leave this console')
        print('\n  --- Property ---')
        print('    has <property>         - print True/False if the model has the property')
        print('    get <property>         - print the porperty value')
        print('    set <property> <value> - push value into the property')
        print('\n  --- File In/Out ---')
        print('    export <file path>     - extract the model and push it into a file')

    @staticmethod
    def extract(UC, cmd):
        if len(cmd) != 1: print('usage: extract')
        else: print(UC.extract())

    @staticmethod
    def quit(UC, cmd): exit(0)

    # --- Property ------------------------------------------------------------#

    @staticmethod
    def has(UC, cmd):
        if len(cmd) != 2: print ('usage: has <property>')
        else: print(UC.has(cmd[1]))

    @staticmethod
    def get(UC, cmd):
        if len(cmd) != 2: print ('usage: get <property>')
        else: print(UC.get(cmd[1]))

    @staticmethod
    def set(UC, cmd):
        if len(cmd) != 3: print('usage: set <property> <value>')
        else:
            try: UC.set(cmd[1], cmd[2])
            except Exception as e: print("error: %s" % str(e))

    # --- File In/Out ---------------------------------------------------------#

    @staticmethod
    def export(UC, cmd):
        if len(cmd) != 2: print('usage: export <file path>')
        else: UC.export(cmd[1])
