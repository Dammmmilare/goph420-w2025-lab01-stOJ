import numpy as np
import unittest
from goph420_lab01.integration import (integrate_gauss,
                                       
                                       ) 

class TestGaussLegendre(unittest.TestCase): 

    def setUp(self):
        """Set up reusable test cases here with results that are known"""
        self.test_cases = [
            (lambda x: 5, (2, 5), 2, 15, 5),
            (lambda x: 2*x + 3, (0, 4), 2, 20, 5),
            (lambda x: x**2, (-2, 2), 3, 8/3, 5),
            (lambda x: x**3 - x**2 + x - 1, (-1, 1), 3, -4/3, 5),
            (lambda x: np.exp(-x**2), (-1, 1), 5, 1.4936, 4),
        ]

        return super().setUp()

    def test_gauss_legendre(self):
        """Test the Gauss-Legendre integration against known results"""
        for f, lims, npts, expected, places in self.test_cases:
            with self.subTest(f=f, lims=lims, npts=npts):
                result = integrate_gauss(f, lims, npts)
                self.assertAlmostEqual(result, expected, places=places)
    
    def test_inalid__function(self):
        """Ensure an error is raised for invalid function"""
        with self.assertRaises(TypeError):
            integrate_gauss(5, (0, 1), 3)
    
    def test_invalid_lims(self):
        """Ensure an error is raised for invalid lims"""
        with self.assertRaises(ValueError):
            integrate_gauss(lambda x: x, (0, 1, 2), 3)
    
    def test_invalid_npts(self):
        """Ensure an error is raised for invalid npts which are out of the allowable range"""
        for invalid_npts in [0, 6, -3, 2.5, "3"]:
            with self.subTest(npts=invalid_npts):
                with self.assertRaises(ValueError):
                    integrate_gauss(lambda x: x, (0, 1), invalid_npts)

if __name__ == "__main__":
    unittest.main()