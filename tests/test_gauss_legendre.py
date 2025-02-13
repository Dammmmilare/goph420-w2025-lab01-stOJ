import numpy as np
import unittest
from goph420_lab01.integration import ( 
    integrate_gauss, 
) 

class TestGaussLegendre(unittest.TestCase): 
    def test_polynomial_exact(self): 
        """ Test the Gauss-Legendre integration of a polynomial up to order 2N - 1"""
        f = lambda x: x**3 - x**2 + x - 1
        result = integrate_gauss(f, -1, 1, 2)
        expected = -4/3
        self.assertAlmostEqual(result, expected, places=10)