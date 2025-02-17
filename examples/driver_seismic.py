import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import numpy as np
import matplotlib.pyplot as plt
from goph420_lab01.integration import (integrate_newton) 

data = np.loadtxt("data/s_wave_data.txt")
time,velocity = data[:,0], data[:,1]


# only using the data we need thanks to this threshold!!
v_max = np.max(np.abs(velocity))
threshold = 0.005 * v_max 
index = np.where(np.abs(velocity) > threshold)[0][-1]

# make space to retain values for error caluclation later
dt = [] 
rela_err_trap = [] 
rela_err_simps = [] 

#evaluate the integrals using trapezoid and simpson rules and differnet interval lengths 


x = time[:index] 
f = velocity[:index] 
int_trap1 = integrate_newton(x, f, alg="trap") 
int_simps1 = integrate_newton(x, f, alg="simp") 

x_2 = time[0:index:2] 
f_2 = velocity[0:index:2] 
int_trap2 = integrate_newton(x_2, f_2, alg="trap") 
int_simps2 = integrate_newton(x_2, f_2, alg="simp") 

x_4 = time[0:index:4] 
f_4 = velocity[0:index:4] 
int_trap4 = integrate_newton(x_4, f_4, alg="trap") 
int_simps4 = integrate_newton(x_4, f_4, alg="simp") 

x_8 = time[0:index:8] 
f_8 = velocity[0:index:8] 
int_trap8 = integrate_newton(x_8, f_8, alg="trap") 
int_simps8 = integrate_newton(x_8, f_8, alg="simp") 

x_16 = time[0:index:16] 
f_16 = velocity[0:index:16] 
int_trap16 = integrate_newton(x_16, f_16, alg="trap") 
int_simps16 = integrate_newton(x_16, f_16, alg="simp") 


# calculate the relative error for each integral 

rela_err_trap1 = np.abs(int_trap8 - int_trap16) / int_trap8 
rela_err_simps1 = np.abs(int_simps8 - int_simps16) / int_simps8
rela_err_trap.append(rela_err_trap1) 
rela_err_simps.append(rela_err_simps1) 
dt.append(x_8[1]-x_8[0]) 

rela_err_trap2 = np.abs(int_trap4 - int_trap8) / int_trap4 
rela_err_simps2 = np.abs(int_simps4 - int_simps8) / int_simps4   
rela_err_trap.append(rela_err_trap2) 
rela_err_simps.append(rela_err_simps2) 
dt.append(x_4[1]-x_4[0]) 

rela_err_trap3 = np.abs(int_trap2 - int_trap4) / int_trap2 
rela_err_simps3 = np.abs(int_simps2 - int_simps4) / int_simps2 
rela_err_trap.append(rela_err_trap3) 
rela_err_simps.append(rela_err_simps3) 
dt.append(x_2[1]-x_2[0]) 

rela_err_trap4 = np.abs(int_trap1 - int_trap2) / int_trap1 
rela_err_simps4 = np.abs(int_simps1 - int_simps2) / int_simps1 
rela_err_trap.append(rela_err_trap4) 
rela_err_simps.append(rela_err_simps4) 
dt.append(x[1]-x[0]) 

# plot the relative error vs the interval length 

plt.loglog(dt, rela_err_trap, label="Trapezoid") 
plt.loglog(dt, rela_err_simps, label="Simpson") 
plt.xlabel("Interval Length") 
plt.ylabel("Relative Error") 
plt.title("Relative Error vs Interval Length") 
plt.legend() 
plt.grid() 
plt.savefig("figures/Trape_SImps_Convergence.png")