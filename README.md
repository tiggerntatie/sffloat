![Python package](https://github.com/tiggerntatie/sffloat/workflows/sffloat%20test%20suite/badge.svg)

# sffloat

The **sffloat** package defines a `SFFloat` class that allows easy floating point computations
that take precision or "significant figures" into account.

## features

* Seamlessly mix `float` and `SFFloat` objects in arithmetic. Standard floating point objects
  are automatically promoted to `SFFloat` when necessary.
* Print and display `SFFloat` objects as if they are standard `float` numbers.
* Compare `SFFloat` objects with floating point numbers to determine equivalence, taking precision
  into account.
* Use `SFFloat` versions of all standard Python math functions.

## example use

### importing SFFloat
```python
from sffloat import SFFloat
```

### calculating circle area using an imprecise radius
```python
# Create a floating point radius value of 3.4 with 2 sig figs
from math import pi
radius = SFFloat(3.4, 2)

# Compute the circle area, with sig figs
area = pi * radius ** 2
print(area)
```
```
36
```
### addition example
```python
a = SFFloat(0.00123, 3)
b = SFFloat(0.1234, 4)
print(a + b)
```
```
0.1246
```
### mix `SFFloat` with `float`
```python
a = SFFloat(0.00123, 3)
print(a + 12.3456789)
```
```
12.34691
```
### use `SFFloat` standard math functions
```python
from math import pi
from sffloat import sfsin as sin

angle = SFFloat(pi / 4, 3)
print(f"The angle is {angle}; its raw value is {angle.value}")
print(f"The sine of {angle} is {sin(angle)}; its raw value is {sin(angle).value}")
```
```
The angle is 0.785; its raw value is 0.7853981633974483
The sine of 0.785 is 0.707; its raw value is 0.7071067811865475
```

## supported functions
If you want to use one of the standard Python math functions while preserving precision then
use any of the following replacement functions. You can either import and use as-is, or import
and assign the standard function name:
```python
from sffloat import sfsin
```
or
```python
from sffloat import sfsin as sin
```

* sfsin replaces sin
* sfcos replaces cos
* sftan replaces tan
* sflog replaces log
* sflog10 replaces log10
* sfasin replaces asin
* sfacos replaces acos
* sfatan replaces atan
* sfatan2 replaces atan2
* sfexp replaces exp
* sfpow replaces pow
* sfsqrt replaces sqrt
* sfdegrees replaces degrees
* sfradians replaces radians

## notes on functionality
* Operation with standard functions is not sophisticated and follows the same rules that are used for
  ordinary multiplication (minimum significant figures propagate as-is).
* When ordinary floating point numbers are used with `SFFloat` values, the floating point values are
  considered to have unlimited precision.
* Addition or subtraction operations on `SFFloat` values may result in "zero" or "negative" significant
  figures. 
* "zero" sig fig values will continue to be used correctly for subsequent addition or subtraction operations.
* "zero" sig fig values will produce an exception when used in a function or multiplication operation.
* "zero" sig fig values will be displayed as '0'.
* The underlying full-precision floating point value of a `SFFloat` object may be accessed with its `.value`
  property.
* The underlying significant figures of a `SFFloat` object may be accessed with its `.sigfigs` property.
* `sffloat` does not attempt to infer precision from initializing value (at the present time).
* `SFFloat` objects display in rounded form using the `sigfig.round` function.
* `SFFloat` objects display in standard format for values between 0.001 and 1000, and for 0, otherwise
  scientific notation is used.
  
## installation
The best way to install `sffloat` is with pip and virtualenv. Create and activate your virtual environment then
install `sffloat` with:
```
pip install sffloat
```

## requirements
`sffloat` depends on `sigfig`, which will be installed automatically when using pip.

## development environment
To begin working with `sffloat` in a development environment:

* Clone this repository and `cd` into it.
* Create a virtual environment: `python3 -m venv ./env`
* Activate the virtual environment: `source ./env/bin/activate`
* Install the dependencies: `pip install -r requirements.txt`

The `./scripts` folder includes a `run_tests.sh` script that will:
* Perform a style check using black.
* Perform a pylint check.
* Execute the test cases using nose.
