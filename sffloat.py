class sffloat(float):
    
    def __new__(self, value, sigfigs=None):
        return float.__new__(self, value)

    def __init__(self, value, sigfigs=None):
        float.__init__(value)
        self.sf = sigfigs

x = sffloat(1.0)
print(type(x))
print(x)