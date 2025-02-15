import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import numpy as np
import matplotlib.pyplot as plt
from data import s_wave_data
from goph420_lab01.integration import (integrate_gauss) 

def probability_density(x):
    return s_wave_data(x, loc=1.5, scale=0.5)

prob = integrate_gauss(probability_density, [4, np.inf], npts=3)
print(f"Probability that S-wave velocity is greater than 4: {prob}")

plt.savefig("figures/probability_density_plot.png")