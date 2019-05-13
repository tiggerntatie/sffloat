class sffloat:

    def __init__(self, value, sigfigs=None):
        self.sf = sigfigs
        self.val = float(value)
        
    def __add__(self, other):
        """
        Implements addition.
        """
        return sffloat(self.val + sffloat(other).val)

    def __mul__(self, other):
        """
        Implements multiplication.
        """
        return sffloat(self.val * sffloat(other).val)
    
    """
    __sub__(self, other)
    Implements subtraction.
    __floordiv__(self, other)
    Implements integer division using the // operator.
    __div__(self, other)
    Implements division using the / operator.
    __truediv__(self, other)
    Implements true division. Note that this only works when from __future__ import division is in effect.
    __mod__(self, other)
    Implements modulo using the % operator.
    __divmod__(self, other)
    Implements behavior for long division using the divmod() built in function.
    __pow__
    Implements behavior for exponents using the ** operator.
    __lshift__(self, other)
    Implements left bitwise shift using the << operator.
    __rshift__(self, other)
    Implements right bitwise shift using the >> operator.
    __and__(self, other)
    Implements bitwise and using the & operator.
    __or__(self, other)
    Implements bitwise or using the | operator.
    __xor__(self, other)
    Implements bitwise xor using the ^ operator.
    """
        

a = sffloat(1.0,2)
b = sffloat(2.0,3)
print(a*b)
print(type(a*b))
print(a.sf)
print(b.sf)