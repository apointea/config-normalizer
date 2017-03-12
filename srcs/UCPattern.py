class UCPattern:

    def __init__(self, filePath):
        self.filePath = filePath
        if not self.filePath.endswith('.yml'):
            self.filepath = self.filePath + '.yml'
        self.dirname = os.path.dirname(self.filePath)
        self.data = yaml.load(open(slef.filePath, 'r'))
