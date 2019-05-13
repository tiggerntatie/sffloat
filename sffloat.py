class sffloat(float):
    
    def __new__(cls, value, sigfigs=None):
        print("new")
        return super().__new__(cls, value)

    def __init__(self, value, sigfigs=None):
        print("init")
        float.__init__(value)
        self.sf = sigfigs

x = sffloat(1.0)
#print(type(x))
#print(x)