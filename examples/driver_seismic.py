import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import numpy as np
import matplotlib.pyplot as plt
from goph420_lab01.integration import (integrate_newton) 

data = np.loadtxt("data/s_wave_data.txt")
x,f = data[:,0], data[:,1]

trap_integral = integrate_newton(x, f,alg="trap")
simp_integral = integrate_newton(x, f,alg="simp")

plt.plot(x, f, label="S-wave data")
plt.legend()
plt.savefig("figures/s_wave_data_plot.png")

print(f"Integral using trapezoidal rule: {trap_integral}")
print(f"Integral using Simpson's rule: {simp_integral}")