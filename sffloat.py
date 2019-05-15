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
        return cls(value, cls._msd_from_val(value) - lsd + 1)

    @staticmethod    
    def _msd_from_val(val):
        """
        Return the position of the most significant digit.
        0 means 1's place, 1 means 10's place, -1 means 0.1's place, etc.
        """
        return floor(log10(abs(val)))

    @classmethod    
    def _lsd_from_val_sf(cls, val, sigfigs):
        """
        Return the position of the least significant digit.
        0 means 1's place, 1 means 10's place, -1 means 0.1's place, etc.
        """
        return cls._msd_from_val(val) - (sigfigs - 1)

    def _msd(self):
        """
        Return the position of the most significant digit.
        0 means 1's place, 1 means 10's place, -1 means 0.1's place, etc.
        """
        return floor(log10(abs(self._val)))
        
    def _lsd(self):
        """
        Return the position of the least significant digit.
        0 means 1's place, 1 means 10's place, -1 means 0.1's place, etc.
        """
        return self._msd() - (self._sf - 1)

    @classmethod
    def _multiplicative_func(cls, f, a, b, rev=False):
        """
        Perform method f on its object a, and other b.
        """
        sfother = cls(b)
        if rev:
            return cls(f(sfother._val, a._val), min(a._sf, sfother._sf))
        else:
            return cls(f(a._val, sfother._val), min(a._sf, sfother._sf))

    @classmethod
    def _additive_func(cls, f, a, b, rev=False):
        """
        Perform method f on its object a, and other b.
        """
        sfother = cls(b)
        lsd = max(a._lsd(), sfother._lsd())
        if rev:
            return cls._sffloat_from_lsd(f(sfother._val, a._val), lsd)
        else:
            return cls._sffloat_from_lsd(f(a._val, sfother._val), lsd)

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
        return self._additive_func(float.__add__, self, other)

    def __radd__(self, other):
        """
        Implements reflected addition.
        """
        return self + other

    def __sub__(self, other):
        """
        Implements subtraction.
        """
        return self._additive_func(float.__sub__, self, other)

    def __rsub__(self, other):
        """
        Implements reflected subtraction.
        """
        return self._additive_func(float.__sub__, self, other, rev=True)
        
    def __mul__(self, other):
        """
        Implements multiplication.
        """
        return self._multiplicative_func(float.__mul__, self, other)

    def __rmul__(self, other):
        """
        Implements reflected multiplication.
        """
        return self._multiplicative_func(float.__mul__, self, other, rev=True)
    
    """
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
        

a = sffloat(1.0,4)
b = sffloat(2.0,9)
print(9-a)
print(a-9)

