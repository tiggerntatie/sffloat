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
        
    def copy(self):
        """
        Return a new instance of sffloat that is a copy.
        """
        return sffloat(self._value, self._sf)
    
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
    def _multiplicative_func(cls, f, a, b, ref=False):
        """
        Perform method f on its object a, and other b.
        """
        sfother = cls(b)
        if ref:
            return cls(f(sfother._val, a._val), min(a._sf, sfother._sf))
        else:
            return cls(f(a._val, sfother._val), min(a._sf, sfother._sf))

    @classmethod
    def _additive_func(cls, f, a, b, ref=False):
        """
        Perform method f on its object a, and other b.
        """
        sfother = cls(b)
        lsd = max(a._lsd(), sfother._lsd())
        if ref:
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
        return self._additive_func(float.__sub__, self, other, ref=True)
        
    def __mul__(self, other):
        """
        Implements multiplication.
        """
        return self._multiplicative_func(float.__mul__, self, other)

    def __rmul__(self, other):
        """
        Implements reflected multiplication.
        """
        return self._multiplicative_func(float.__mul__, self, other, ref=True)

    def __floordiv__(self, other):
        """
        Implements integer division using the // operator.
        """
        return self._multiplicative_func(float.__floordiv__, self, other)

    def __rfloordiv__(self, other):
        """
        Implements reflected integer division using the // operator.
        """
        return self._multiplicative_func(float.__floordiv__, self, other, ref=True)

    def __div__(self, other):
        """
        Implements division using the / operator.
        """
        return self._multiplicative_func(float.__div__, self, other)

    def __rdiv__(self, other):
        """
        Implements reflected division using the / operator.
        """
        return self._multiplicative_func(float.__rdiv__, self, other)

    def __truediv__(self, other):
        """
        Implements true division. Note that this only works when from __future__ import division is in effect.
        """
        return self._multiplicative_func(float.__truediv__, self, other)
    
    def __rtruediv__(self, other):
        """
        Implements reflected true division. Note that this only works when from __future__ import division is in effect.
        """
        return self._multiplicative_func(float.__rtruediv__, self, other, ref=True)

    def __pow__(self, other):
        """
        Implements behavior for exponents using the ** operator.
        """
        return self._multiplicative_func(float.__pow__, self, other)

    def __rpow__(self, other):
        """
        Implements behavior for reflected exponents using the ** operator.
        """
        return self._multiplicative_func(float.__pow__, self, other, True)

    def __eq__(self, other):
        """
        Implements equality operator: == 
        Checks for matching value only.
        """
        return self._val == sffloat(other)._val
        
    def __ne__(self, other):
        """
        Implements not equal operator: !=
        Checks for mismatching value only.
        """
        return not (self == other)
 
    def __cmp__(self, other):
        """
        Implements the comparison operation: 
        -integer if self < other
        0 if self == other
        +integer if self > other
        """
        if self > other:
            return 1
        elif self < other:
            return -1
        else:
            return 0
        
    def __lt__(self, other):
        """
        Implements less than operator: <
        This compares the raw values without regard to sigfigs.
        """
        return self._val < sffloat(other)._val
        
    def __gt__(self, other):
        """
        Implements greater than operator: >
        This compares the raw values without regard to sigfigs.
        """
        return self._val > sffloat(other)._val
        
    def __le__(self, other):
        """
        Implements less than operator: <
        This compares the raw values without regard to sigfigs.
        """
        return self._val <= sffloat(other)._val
        
    def __ge__(self, other):
        """
        Implements greater than operator: >
        This compares the raw values without regard to sigfigs.
        """
        return self._val >= sffloat(other)._val
        
    def __pos__(self):
        """
        Implements the unary + operator. This does nothing.
        """
        return self
        
    def __neg__(self):
        """
        Implements the unary - operator. Makes value negative.
        """
        retval = self.copy()
        retval._val = -retval._val
        return retval
        
    def __abs__(self):
        """
        Implements the absolute value function. 
        """
        retval = self.copy()
        retval._val = abs(retval._val)
        return retval
        
    
        
        
    
    

a = sffloat(1.0,4)
b = sffloat(2.0,9)
c = sffloat(3,3)
print(9-a)
print(a-9)
print(c)
print(a/b)
print(b**c)

from math import sin, degrees

t = sffloat(3.14,3)
print(sin(t))
print(degrees(t))
print(a < b)
