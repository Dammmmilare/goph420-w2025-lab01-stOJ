import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import numpy as np
import unittest
import matplotlib.pyplot as plt
from goph420_lab01.integration import (integrate_gauss) 

def main():
    unittest.main()

if __name__ == "__main__":
    main()