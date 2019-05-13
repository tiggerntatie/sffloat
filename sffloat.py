import math


def to_precision(x,p):
    """
    returns a string representation of x formatted with a precision of p
    
    Based on work by Randle Taylor here:
    http://randlet.com/blog/python-significant-figures-format/
    
    Randle credits:
    Based on the webkit javascript implementation taken from here:
    https://code.google.com/p/webkit-mirror/source/browse/JavaScriptCore/kjs/number_object.cpp
    """

    x = float(x)

    if x == 0.:
        return "0." + "0"*(p-1)

    out = []

    if x < 0:
        out.append("-")
        x = -x

    e = int(math.log10(x))
    tens = math.pow(10, e - p + 1)
    n = math.floor(x/tens)

    if n < math.pow(10, p - 1):
        e = e -1
        tens = math.pow(10, e - p+1)
        n = math.floor(x / tens)

    if abs((n + 1.) * tens - x) <= abs(n * tens -x):
        n = n + 1

    if n >= math.pow(10,p):
        n = n / 10.
        e = e + 1

    #m = "%.*g" % (p, n)
    m = "{0:{1}g}".format(n, p)

    if e < -2 or e >= p:
        out.append(m[0])
        if p > 1:
            out.append(".")
            out.extend(m[1:p])
        out.append('e')
        if e > 0:
            out.append("+")
        out.append(str(e))
    elif e == (p -1):
        out.append(m)
    elif e >= 0:
        out.append(m[:e+1])
        if e+1 < len(m):
            out.append(".")
            out.extend(m[e+1:])
    else:
        out.append("0.")
        out.extend(["0"]*(-(e+1)))
        out.append(m)

    return "".join(out)

class sffloat:

    def __init__(self, value, sigfigs=None):
        if sigfigs is not None and sigfigs <= 0:
            raise ValueError("Invalid value for sigfigs.")
        try:
            if sigfigs:
                self.sf = sigfigs
            else:
                self.sf = value.sf
            self.val = value.val
        except AttributeError:
            self.sf = sigfigs
            self.val = float(value)
            
    
    def __repr__(self):
        if self.sf is None:
            return "sffloat({0})".format(self.val)
        else:
            return "sffloat({0},{1})".format(self.val, self.sf)
            
    def __str__(self):
        if self.sf is None:
            return str(self.val)
        else:
            return to_precision(self.val, self.sf)

    def __float__(self):
        return self.val
        
    def __add__(self, other):
        """
        Implements addition.
        """
        return sffloat(self.val + sffloat(other).val)

    def __mul__(self, other):
        """
        Implements multiplication.
        """
        sfother = sffloat(other)
        if sfother.sf is None:
            newsf = self.sf
        else:
            newsf = min(self.sf, sfother.sf)
        return sffloat(float(self) * sffloat(other).val, newsf)

    def __rmul__(self, other):
        """
        Implements reflected multiplication.
        """
        return self * other
    
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
    
    
    __radd__(self, other)
    Implements reflected addition.
    __rsub__(self, other)
    Implements reflected subtraction.
    __rfloordiv__(self, other)
    Implements reflected integer division using the // operator.
    __rdiv__(self, other)
    Implements reflected division using the / operator.
    __rtruediv__(self, other)
    Implements reflected true division. Note that this only works when from __future__ import division is in effect.
    __rmod__(self, other)
    Implements reflected modulo using the % operator.
    __rdivmod__(self, other)
    Implements behavior for long division using the divmod() built in function, when divmod(other, self) is called.
    __rpow__
    Implements behavior for reflected exponents using the ** operator.
    __rlshift__(self, other)
    Implements reflected left bitwise shift using the << operator.
    __rrshift__(self, other)
    Implements reflected right bitwise shift using the >> operator.
    __rand__(self, other)
    Implements reflected bitwise and using the & operator.
    __ror__(self, other)
    Implements reflected bitwise or using the | operator.
    __rxor__(self, other)
    Implements reflected bitwise xor using the ^ operator.    
    """
        

a = sffloat(1.0,2)
b = sffloat(2.0,3)
print(a*b)
print(type(a*b))
print(b*1)
print(2000001*b)
