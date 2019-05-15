from math import log10, floor
import to_precision




class sffloat:
    
    inf = float('inf')

    def __new__(cls, val, sigfigs=None):
        if type(val) is cls and sigfigs is None:
            return val
        else:
            return super().__new__(cls)

    def __init__(self, value, sigfigs=None):
        if sigfigs is not None and sigfigs <= 0 and sigfigs is not float('inf'):
            raise ValueError("Invalid value for sigfigs.")
        elif sigfigs is None and self is value:
            return  # just passthru
        if sigfigs is not None:
            self._sf = sigfigs
        else:
            self._sf = self.inf
        self._val = float(value)
        
    @classmethod
    def _sffloat_from_lsd(cls, value, lsd):
        """
        Return a new sffloat instance for a given value and lsd place
        """
        return cls(value, self._msd(value) - lsd + 1)
    
    @staticmethod    
    def _msd_from_val(val):
        """
        Return the position of the most significant digit.
        0 means 1's place, 1 means 10's place, -1 means 0.1's place, etc.
        """
        return floor(log10(val))

    @staticmethod    
    def _lsd_from_val_sf(val, sigfigs):
        """
        Return the position of the least significant digit.
        0 means 1's place, 1 means 10's place, -1 means 0.1's place, etc.
        """
        return self._msd(val) - (sigfigs - 1)

    def _msd(self):
        """
        Return the position of the most significant digit.
        0 means 1's place, 1 means 10's place, -1 means 0.1's place, etc.
        """
        return floor(log10(self._val))
        
    def _lsd(self):
        """
        Return the position of the least significant digit.
        0 means 1's place, 1 means 10's place, -1 means 0.1's place, etc.
        """
        return self._msd() - (self._sf - 1)

    def __repr__(self):
        if self._sf is self.inf:
            return "sffloat({0})".format(self._val)
        else:
            return "sffloat({0},{1})".format(self._val, self._sf)
            
    def __str__(self):
        if self._sf is self.inf:
            return str(self._val)
        else:
            return to_precision.to_precision(self._val, self._sf)

    def __float__(self):
        return self._val
        
    def __add__(self, other):
        """
        Implements addition.
        """
        sfother = type(self)(other)
        lsd = max(self._lsd(), sfother._lsd())
        return self._sffloat_from_lsd(self._val + sfother._val, lsd)

    def __radd__(self, other):
        """
        Implements reflected addition.
        """
        return self + other
        
    def __mul__(self, other):
        """
        Implements multiplication.
        """
        sfother = type(self)(other)
        newsf = self.inf
        return type(self)(self._val*sfother._val, min(self._sf, sfother._sf))
    
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
print(a+b)
print(a+0.1)
print(a+0.01)
print(a+0.001)
print(0.1+a)
print(0.001+a)