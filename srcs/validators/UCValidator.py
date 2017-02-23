class UCValidator:

    def extractStrProp(self, data, prop):
        if prop in data:
            setattr(self, prop, str(data[prop]))
        else:
            setattr(self, prop, False)

    def extractIntProp(self, data, prop):
        if prop in data:
            setattr(self, prop, int(data[prop]))
        else:
            setattr(self, prop, False)
