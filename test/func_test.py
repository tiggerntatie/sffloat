from math import *
import unittest
from sffloat import *

class TestFuncMethods(unittest.TestCase):
    def test_sfsin(self):
        self.assertEqual(str(sfsin(SFFloat(1.234,2))), '0.94')
    
    def test_sfcos(self):
        self.assertEqual(str(sfcos(SFFloat(1.234,2))), '0.33')
        
    def test_sftan(self):
        self.assertEqual(str(sftan(SFFloat(1.234,2))), '2.9')

    def test_sflog(self):
        self.assertEqual(str(sflog(SFFloat(1.234,2))), '0.21')

    def test_sflog10(self):
        self.assertEqual(str(sflog10(SFFloat(1.234,2))), '0.091')

    def test_sftan(self):
        self.assertEqual(str(sftan(SFFloat(1.234,2))), '2.9')

    def test_sfasin(self):
        self.assertEqual(str(sfasin(SFFloat(0.1234,2))), '0.12')

    def test_sfacos(self):
        self.assertEqual(str(sfacos(SFFloat(0.1234,2))), '1.4')

    def test_sfatan(self):
        self.assertEqual(str(sfatan(SFFloat(1.234,2))), '0.89')

    def test_sfatan2(self):
        self.assertEqual(str(sfatan2(SFFloat(1.234,2), SFFloat(2.345, 3))), '0.48')

    def test_sfexp(self):
        self.assertEqual(str(sfexp(SFFloat(0.1234,2))), '1.1')

    def test_sfpow(self):
        self.assertEqual(str(sfpow(SFFloat(1.234,2), SFFloat(2.345, 3))), '1.6')

    def test_sfsqrt(self):
        self.assertEqual(str(sfsqrt(SFFloat(0.1234,2))), '0.35')

    def test_sfdegrees(self):
        self.assertEqual(str(sfdegrees(SFFloat(0.1234,2))), '7.1')

    def test_sfradians(self):
        self.assertEqual(str(sfradians(SFFloat(0.1234,2))), '0.0022')



