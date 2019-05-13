class sffloat(float):
    def __new__(self, value, extra):
        return float.__new__(self, value)
    def __init__(self, value, extra):
        float.__init__(value)
        self.extra = extra
