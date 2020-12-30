"""
The example module demonstrates basic use of the SFFloat class for performing
floating point arithmetic while tracking significant figures.
"""
from math import pi
from sffloat import SFFloat
from sffloat import sfsin as sin

# Create a floating point radius value with 2 sig figs
radius = SFFloat(3.4, 2)

# Compute the circle area, with sig figs
area = pi * radius ** 2
print(area)  # prints 36

# Addition example
a = SFFloat(0.00123, 3)
b = SFFloat(0.1234, 4)
print(a + b)  # prints 0.1246

# Mix ordinary floats and SFFloats
print(a + 0.12345678)  # prints 0.12469

# Use with wrapped math functions (note the sfsin import above!)
print(sin(SFFloat(pi / 4, 3)))  # prints 0.707


angle = SFFloat(pi / 4, 3)
print(f"The angle is {angle} radians; its raw value is {angle.value} radians")
print(f"The sine of {angle} is {sin(angle)}; its raw value is {sin(angle).value}")
