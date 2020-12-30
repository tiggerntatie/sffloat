"""
The sffloat module defines the :class:`SFFloat` class which tracks significant figures
in floating point calculations. It also defines wrapper functions for Python's standard
mathematics functions.
"""

import math
import warnings
import sigfig

warnings.simplefilter("ignore")


class SFFloat:
    """
    The sffloat :class:`SFFloat` class implements a replacement of the builtin float that
    can define floating point type values with an additional significant figures attribute.
    Arithmetic operations performed with the :class: `SFFloat` types track and maintain
    the correct number of significant figures and will display the proper rounded value
    when printing or converting to string.

    :Required Arguments:
        * **val** [float or str] The numeric value of the new instance.

    :Optional Arguments:
        * **sigfigs** [int] The number of significant digits of the new instance.
            This argument should be used in order to use the :class:`SFFloat`
            significant figures tracking. If this argument is omitted, or if the
            argument is set equal to `float('inf')` then the resulting
            :class:`SFFloat` instance will have unlimited significant digits.

    :Optional Keyword Arguments:
        * **lsd** [int] The place of the least significant digit in the value. The
            ones place corresponds to zero, with increasing negative values indicating
            digits to the right of the ones place and increasing positive values
            indicating digits to the left of the ones place. Note that the **sigfigs**
            argument and the **lsd** argument may not be used at the same time."""

    inf = float("inf")

    def __new__(cls, val, sigfigs=None, **_):
        if isinstance(val, cls) and sigfigs is None:
            return val
        return super().__new__(cls)

    def __init__(self, value, sigfigs=None, **kwargs):
        if sigfigs and not isinstance(sigfigs, int) and not sigfigs is float("inf"):
            raise ValueError("Invalid value for sigfigs.")
        if sigfigs is None and self is value:
            return  # just passthru
        self._lsd = kwargs.get("lsd", None)
        if self._lsd is not None and sigfigs is not None:
            raise ValueError("Can not specify both lsd and sigfigs.")
        # passing value only - infinite sigfigs
        if self._lsd is None and sigfigs is None:
            self._sf = self.inf
        # passing lsd value, set _sf to None
        elif self._lsd is not None:
            self._sf = None
        # sigfigs must be set - figure out lsd
        else:
            self._sf = None
            self._lsd = self._msd_from_val(value) - (sigfigs - 1)
        self._val = float(value)

    def copy(self):
        """
        Return a new instance of SFFloat that is a copy.
        """
        return type(self)(self._val, lsd=self._lsd)

    def equivalent_to_float(self, other):
        """
        Return True if other float value is
        equivalent to self, when taking significant figures
        into account.

        Ex. SFFloat(3.1415926, 3).equivalent_to(3.142) --> True
        """
        sfother = type(self)(other, self.sigfigs)
        return str(self) == str(sfother)

    @property
    def sigfigs(self):
        """
        Return the number of significant figures for this value
        """
        if self._sf is self.inf:
            return self._sf
        return self._msd_from_val(self._val) - self._lsd + 1

    @property
    def value(self):
        """
        Return the full-precision internal value
        """
        return self._val

    @property
    def lsd(self):
        """
        Return the position of the least significant digit.
        0 means 1's place, 1 means 10's place, -1 means 0.1's place, etc.
        """
        return self._lsd

    # Wrappers for mathematics functions

    @classmethod
    def funcwrapper(cls, func, arg):
        """
        Generic wrapper for functions that support SFFloat arguments
        """
        try:
            return cls(func(arg), arg.sigfigs)
        except AttributeError:
            return func(arg)

    @classmethod
    def funcwrapper2(cls, func, arg1, arg2):
        """
        Generic wrapper for functions that support sffloat arguments
        """
        if not isinstance(arg1, cls) and not isinstance(arg2, cls):
            return func(arg1, arg2)
        return cls(func(arg1, arg2), min(cls(arg1).sigfigs, cls(arg2).sigfigs))

    @staticmethod
    def _msd_from_val(val):
        """
        Return the position of the most significant digit.
        0 means 1's place, 1 means 10's place, -1 means 0.1's place, etc.
        """
        if not val:
            return 0
        return math.floor(math.log10(abs(val)))

    def _msd(self):
        """
        Return the position of the most significant digit.
        0 means 1's place, 1 means 10's place, -1 means 0.1's place, etc.
        """
        return math.floor(math.log10(abs(self._val)))

    @classmethod
    def _multiplicative_func(cls, func, arg1, arg2):
        """
        Perform method func on its object arg1, and other arg2.
        """
        sfother = cls(arg2)
        minsigfig = min(arg1.sigfigs, sfother.sigfigs)
        if minsigfig <= 0:
            raise ValueError(
                f"Precision of {func} with zero sigfig operand is undefined."
            )
        return cls(func(arg1.value, sfother.value), minsigfig)

    @classmethod
    def _additive_func(cls, func, arg1, arg2):
        """
        Perform method func on its object arg1, and other arg2.
        """
        sfother = cls(arg2)
        if arg1.sigfigs is cls.inf:
            lsd = sfother.lsd
        elif sfother.sigfigs is cls.inf:
            lsd = arg1.lsd
        else:
            lsd = max(arg1.lsd, sfother.lsd)
        return cls(func(arg1.value, sfother.value), lsd=lsd)

    def __repr__(self):
        if self._sf is self.inf:
            return f"{type(self).__name__}({self._val})"
        return f"{type(self).__name__}({self._val},{self.sigfigs})"

    def __str__(self):
        if self._sf is self.inf:
            return str(self._val)
        sigfigs = self.sigfigs
        if sigfigs <= 0:
            return "0"
        nottype = "sci"
        if 0.001 < abs(self._val) < 1000 or self._val == 0.0:
            nottype = "std"
        return sigfig.round(self._val, self.sigfigs, notation=nottype)

    def __format__(self, format_spec):
        if format_spec == "":
            return str(self)
        return float(str(self)).__format__(format_spec)

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
        return self._additive_func(float.__rsub__, self, other)

    def __mul__(self, other):
        """
        Implements multiplication.
        """
        return self._multiplicative_func(float.__mul__, self, other)

    def __rmul__(self, other):
        """
        Implements reflected multiplication.
        """
        return self._multiplicative_func(float.__rmul__, self, other)

    def __truediv__(self, other):
        """
        Implements true division.
        """
        return self._multiplicative_func(float.__truediv__, self, other)

    def __rtruediv__(self, other):
        """
        Implements reflected true division.
        """
        return self._multiplicative_func(float.__rtruediv__, self, other)

    def __pow__(self, other):
        """
        Implements behavior for exponents using the ** operator.
        """
        return self._multiplicative_func(float.__pow__, self, other)

    def __rpow__(self, other):
        """
        Implements behavior for reflected exponents using the ** operator.
        """
        return self._multiplicative_func(float.__rpow__, self, other)

    def __eq__(self, other):
        """
        Implements equality operator: ==
        Checks for matching value and sigfigs.
        """
        other = SFFloat(other)
        return self._val == other.value and self.sigfigs == other.sigfigs

    def __ne__(self, other):
        """
        Implements not equal operator: !=
        Checks for mismatching value or sigfig.
        """
        other = SFFloat(other)
        return self._val != other.value or self.sigfigs != other.sigfigs

    def __cmp__(self, other):
        """
        Implements the comparison operation:
        -integer if self < other
        0 if self == other
        +integer if self > other
        """
        if self > other:
            return 1
        if self < other:
            return -1
        return 0

    def __lt__(self, other):
        """
        Implements less than operator: <
        This compares the raw values and considers sig figs
        """
        return self._val < type(self)(other)._val and self != other

    def __gt__(self, other):
        """
        Implements greater than operator: >
        This compares the raw values and considers sig figs
        """
        return self._val > type(self)(other)._val and self != other

    def __le__(self, other):
        """
        Implements less than operator: <
        This compares the raw values and considers sig figs
        """
        return self._val < type(self)(other)._val or self == other

    def __ge__(self, other):
        """
        Implements greater than operator: >
        This compares the raw values and considers sig figs
        """
        return self._val > type(self)(other)._val or self == other

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


sfsin = lambda x: SFFloat.funcwrapper(math.sin, x)
sfcos = lambda x: SFFloat.funcwrapper(math.cos, x)
sftan = lambda x: SFFloat.funcwrapper(math.tan, x)
sflog = lambda x: SFFloat.funcwrapper(math.log, x)
sflog10 = lambda x: SFFloat.funcwrapper(math.log10, x)
sfasin = lambda x: SFFloat.funcwrapper(math.asin, x)
sfacos = lambda x: SFFloat.funcwrapper(math.acos, x)
sfatan = lambda x: SFFloat.funcwrapper(math.atan, x)
sfatan2 = lambda x, y: SFFloat.funcwrapper2(math.atan2, x, y)
sfexp = lambda x: SFFloat.funcwrapper(math.exp, x)
sfpow = lambda x, y: SFFloat.funcwrapper2(math.pow, x, y)
sfsqrt = lambda x: SFFloat.funcwrapper(math.sqrt, x)
sfdegrees = lambda x: SFFloat.funcwrapper(math.degrees, x)
sfradians = lambda x: SFFloat.funcwrapper(math.radians, x)
