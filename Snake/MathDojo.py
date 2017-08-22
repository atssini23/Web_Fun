import arithmetic
class MathDojo(object):
    def __init__(self,data,method=None):
        self.data = data
        self.method = method

    def add(self):
        return self

    def subtract(self):
        return self

    def results(self):
        return self

MathDojo().add(2).add(2, 5).subtract(3, 2).result
