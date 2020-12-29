from math import *
import unittest
from sffloat import SFFloat

class TestOperMethods(unittest.TestCase):
    def test_add(self):
        # basic addition
        a = SFFloat(123456)
        b = SFFloat(123456, 3)
        c = SFFloat(123456, 2)
        self.assertEqual(str(a+b), '2.47E5')
        self.assertEqual(str(b+a), '2.47E5')
        self.assertEqual(str(123456+b), '2.47E5')
        self.assertEqual(str(b+123456), '2.47E5')
        self.assertEqual(str(b+c), '2.5E5')
        self.assertEqual(str(c+b), '2.5E5')
        d = SFFloat(0.123456)
        e = SFFloat(0.123456, 3)
        f = SFFloat(0.123456, 2)
        self.assertEqual(str(d+e), '0.247')
        self.assertEqual(str(e+d), '0.247')
        self.assertEqual(str(0.123456+e), '0.247')
        self.assertEqual(str(e+0.123456), '0.247')
        self.assertEqual(str(e+f), '0.25')
        self.assertEqual(str(f+e), '0.25')
        
    def test_sub(self):
        # basic subtraction
        a = SFFloat(123456)
        b = SFFloat(654321, 3)
        c = SFFloat(123456, 2)
        self.assertEqual(str(a-b), '-5.31E5')
        self.assertEqual(str(b-a), '5.31E5')
        self.assertEqual(str(123456-b), '-5.31E5')
        self.assertEqual(str(b-123456), '5.31E5')
        self.assertEqual(str(b-c), '5.3E5')
        self.assertEqual(str(c-b), '-5.3E5')
        d = SFFloat(0.123456)
        e = SFFloat(0.123456, 3)
        f = SFFloat(0.123456, 2)
        self.assertEqual(str(d-e), '0.247')
        self.assertEqual(str(e-d), '0.247')
        self.assertEqual(str(0.123456-e), '0.247')
        self.assertEqual(str(e-0.123456), '0.247')
        self.assertEqual(str(e-f), '0.25')
        self.assertEqual(str(f-e), '0.25')
        