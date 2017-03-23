from .UCException import *

class UCDataStructure:

    def buildProperty(self, fname, cnt):
        # Is 'dict' and has a property 'cmd'
        if isinstance(cnt, dict) and cnt.get('cmd', False):
            cmd = cnt.get('cmd')
            if cmd == 'include':
                return __buildInclude(fname, cnt)
            elif cmd == 'pattern':
                return __buildPattern(fname, cnt)
            else:
                raise UCException("unknown command: '%s'" % cnt['cmd'])
        # Is 'list' - implicit pattern
        elif isinstance(cnt, list):
            return UCPattern(fname, cnt, self.dirName)
        # Else - it's consider as a field
        else:
            return UCField(fname, cnt)

    def __buildInclude(self, fname, cnt):
        if cnt.get('path', False):
            modelPath = os.path.join(self.dirName, cnt['path'])
            return UCModel(modelPath)
        raise UCException("include, 'path' param. not found : '%s'" % fname)

    def __buildPattern(self, fname, cnt):
        if cnt.get('data', False):
            return UCPattern(fname, cnt.get('data'), self.dirName, cnt)
        raise UCException("pattern, 'data' param. not found : '%s'" % fname)
