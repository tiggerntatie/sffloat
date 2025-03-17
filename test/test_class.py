from math import *
import unittest
from sffloat import SFFloat

class TestClassMethods(unittest.TestCase):
    def test_create(self):
        # basic string representations, with and without sig figs
        a = SFFloat(1)
        self.assertEqual(a.__repr__(), 'SFFloat(1.0)')
        self.assertEqual(str(a), '1.0')
        b = SFFloat(1,1)
        self.assertEqual(b.__repr__(), 'SFFloat(1.0,1)')
        self.assertEqual(str(b), '1')
        c = SFFloat(1.234, lsd=-1)
        self.assertEqual(c.__repr__(), 'SFFloat(1.234,2)')
        self.assertEqual(str(c), '1.2')

    def test_copy(self):
        # copy method
        b = SFFloat(1,1)
        bc = b.copy()
        self.assertEqual(b, bc)
        self.assertEqual(b.sigfigs, bc.sigfigs)
        self.assertEqual(b.value, bc.value)
        
    def test_equivalent(self):
        # equivalent_to_float method
        a = SFFloat(pi, 4)
        b = 3.14
        c = 3.142
        d = 3.1415
        self.assertFalse(a.equivalent_to_float(b))
        self.assertTrue(a.equivalent_to_float(c))
        self.assertTrue(a.equivalent_to_float(d))
        
    def test_sigfigs(self):
        # sigfigs property
        a = SFFloat(pi, 4)
        self.assertEqual(a.sigfigs, 4)
        b = SFFloat(pi)
        self.assertEqual(b.sigfigs, float('inf'))
        
    def test_value(self):
        # value property
        a = SFFloat(pi, 4)
        self.assertEqual(a.value, pi)
        
    def test_format(self):
        # support for string formatting
        a = SFFloat(pi, 4)
        self.assertEqual(f"{a:0.2f}", "3.14")
        
    def test_float(self):
        # support for converting to float
        a = SFFloat(pi, 4)
        self.assertEqual(float(a), pi)
      
        
        