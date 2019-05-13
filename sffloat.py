class sffloat(float):
    def __new__(cls, value, sigfigs=None):
        return super().__new__(cls, value)

    def __init__(self, value, sigfigs=None):
        float.__init__(value)
        self.sf = sigfigs

a = sffloat(1.0,2)
b = sffloat(2.0,3)
print(a*b)
print(type(a*b))
print(a.sf)
print(b.sf)