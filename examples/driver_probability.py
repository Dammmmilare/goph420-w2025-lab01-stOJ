import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from goph420_lab01.integration import (integrate_gauss) 

file_path = "data/s_wave_data.txt"
s_wave_data = np.loadtxt(file_path)

def probability_density(x):
    return norm.pdf(x, loc=1.5, scale=0.5)

prob = integrate_gauss(probability_density, [4, np.inf], npts=3)
print(f"Probability that S-wave velocity is greater than 4: {prob}")

plt.plot(s_wave_data)
plt.savefig("figures/probability_density_plot.png")