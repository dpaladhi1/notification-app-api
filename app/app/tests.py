"""
run simple test
"""
from django.test import SimpleTestCase
from app import calc

class calcTests(SimpleTestCase):
    """ test simple add function"""
    def test_calc_add(self):
        res= calc.add(5,5)
        self.assertEqual(res,10)