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
        self.assertEqual(str(d-e), '0.000')
        self.assertEqual(str(e-d), '0.000')
        self.assertEqual(str(0.123456-e), '0.000')
        self.assertEqual(str(e-0.123456), '0.000')
        self.assertEqual(str(e-f), '0.00')
        self.assertEqual(str(f-e), '0.00')
        
    def test_mul(self):
        # basic multiplication
        a = SFFloat(pi, 2)
        b = SFFloat(2, 3)
        c = SFFloat(2E-10, 4)
        self.assertEqual(str(a*b), '6.3')
        self.assertEqual(str(b*a), '6.3')
        self.assertEqual(str(pi*b), '6.28')
        self.assertEqual(str(b*pi), '6.28')
        self.assertEqual(str(c*pi), '6.283E-10')
        self.assertEqual(str(pi*c), '6.283E-10')
        self.assertEqual(str(b*c), '4.00E-10')
        self.assertEqual(str(c*b), '4.00E-10')
        d = SFFloat(-2,4)
        self.assertEqual(str(b*d), '-4.00')
        self.assertEqual(str(d*b), '-4.00')
        
    def test_div(self):
        # basic division
        a = SFFloat(pi, 2)
        b = SFFloat(2, 3)
        c = SFFloat(2E-10, 4)
        self.assertEqual(str(a/b), '1.6')
        self.assertEqual(str(b/a), '0.64')
        self.assertEqual(str(pi/b), '1.57')
        self.assertEqual(str(b/pi), '0.637')
        self.assertEqual(str(a/c), '1.6E10')
        self.assertEqual(str(c/a), '6.4E-11')
        self.assertEqual(str(-pi/c), '-1.571E10')
        self.assertEqual(str(c/(-pi)), '-6.366E-11')
        
    def test_pos(self):
        # ** operator 
        a = SFFloat(2.1234, 2)
        b = SFFloat(2, 3)
        self.assertEqual(str(b**a), '4.4')
        self.assertEqual(str(2**a), '4.4')
        self.assertEqual(str(a**2), '4.5')
        self.assertEqual(str(b**2), '4.00')
        self.assertEqual(str(2**b), '4.00')
        
    def test_eq(self):
        # == operator
        aa = SFFloat(1.234, 3)
        a = SFFloat(1.234, 3)
        b = SFFloat(1.234, 2)
        self.assertTrue(a == aa)
        self.assertFalse(a == b)
        self.assertFalse(1.234 == a)
        self.assertFalse(a == 1.234)
        
    def test_ne(self):
        # != operator
        aa = SFFloat(1.234, 3)
        a = SFFloat(1.234, 3)
        b = SFFloat(1.234, 2)
        self.assertFalse(a != aa)
        self.assertTrue(a != b)
        self.assertTrue(1.234 != a)
        self.assertTrue(a != 1.234)
        
    def test_cmp(self):
        # comparison operator
        a = SFFloat(1.234, 3)
        b = SFFloat(1.200, 3)
        c = SFFloat(1.23456, 3)
        d = 1.234
        x = [a, d, b, c]
        xs = sorted(x)
        self.assertEqual(str(xs), '[SFFloat(1.2,3), SFFloat(1.234,3), 1.234, SFFloat(1.23456,3)]')
        
    def test_ltgt(self):
        # lt and gt operators
        a = SFFloat(1.234, 3)
        b = SFFloat(1.200, 3)
        c = SFFloat(1.234, 4)
        d = 1.234
        self.assertTrue(a > b)
        self.assertTrue(b < a)
        self.assertFalse(a < b)
        self.assertFalse(b > a)
        self.assertFalse(c > a)
        self.assertFalse(a < c)
        self.assertTrue(b < d)
        self.assertFalse(d < b)
        self.assertTrue(d > b)
        self.assertFalse(b > d)
        
    def test_lege(self):
        # le and ge operators
        a = SFFloat(1.234, 3)
        b = SFFloat(1.200, 2)
        c = SFFloat(1.234, 3)
        d = 1.234
        self.assertTrue(a >= b)
        self.assertTrue(b <= a)
        self.assertFalse(a <= b)
        self.assertFalse(b >= a)
        self.assertTrue(c >= a)
        self.assertTrue(a <= c)
        self.assertTrue(b <= d)
        self.assertFalse(d <= b)
        self.assertTrue(d >= b)
        self.assertFalse(b >= d)
        
    def test_neg(self):
        # neg operator
        a = SFFloat(1.234, 3)
        self.assertEqual(str(-a), '-1.23')
        
    def test_abs(self):
        # abs operator
        a = SFFloat(-1.234, 3)
        self.assertEqual(str(abs(a)), '1.23')
        
        
        