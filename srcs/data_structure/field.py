class field:

    def __init__(self, value='', validator=False):
        self.validator = validator
        self.setValue(value)

    def setValue(self, newValue):
        if self.validator:
            print('start validation')
        self.value = newValue

    def export(self):
        return (self.value)
