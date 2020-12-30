from math import *
import unittest
from sffloat import SFFloat

class TestExceptions(unittest.TestCase):
    def test_create(self):
        # basic silly things
        self.assertRaises(ValueError, lambda: SFFloat(1.0, 1.0))
        self.assertRaises(ValueError, lambda: SFFloat(1.0, "1"))
        self.assertRaises(ValueError, lambda: SFFloat(1.0, 1, lsd=-1))

    # precision underflow
    def test_edgecases(self):
        a = SFFloat(1.23456, 3)
        b = SFFloat(1.23567, 3)
        self.assertEqual(str(a-b), '0')
        self.assertRaises(ValueError, lambda: 3*(a-b))
        