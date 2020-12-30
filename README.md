# sffloat

The **sffloat** package defines a `SFFloat` class that allows easy floating point computations
that take precision or "significant figures" into account.

## features

* Seamlessly mix `float` and `SFFloat` objects in arithmetic. Standard floating point objects
  are automatically promoted to `SFFloat` when necessary.
* Print and display `SFFloat` objects as if they are standard `float` numbers.
* Compare `SFFloat` objects with floating point numbers to determine equivalence, taking precision
  into account.
  
## example use

### importing SFFloat
```python
from sffloat import SFFloat
```

### calculating circle area using an imprecise radius
```python
# Create a floating point radius value of 3.4 with 2 sig figs
radius = SFFloat(3.4, 2)

# Compute the circle area, with sig figs
area = pi * radius ** 2
print(area)
```
```
36
```
