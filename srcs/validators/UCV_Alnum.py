from .UCVAbastract import UCVAbastract

class UCVAlnum(UCVAbastract):

    def emsg(self, value):
        return("validator 'Alnum' reject '%s'" % str(value))

    def child_check(self, value):
        if not str(value).isalnum(): return False
        return True
