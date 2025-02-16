import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from goph420_lab01.integration import (integrate_gauss) 

def standard_normal(z): 
    """ 
    Standard normal distribution  
    calculated using equation 17 form the lab
    """
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * z**2) 


def seismic_prob(mag, mean, stdev, npts): 
    """ 
    for part 1 of question 8 
    
    compute the probability of an earthquake with a magnitude greater than 4.0 
    """

    # equation 18 from the lab 

    z = (mag - mean) / stdev 

    # integration limits 
    lims = [z, 10] 

    return integrate_gauss(standard_normal, lims, npts) 

def probability_length(L1, L2, L_mean, stdev, npts): 
    """ 
    for part 2 of question 8 
    
    compute the probability of a length of a bridge being between L1 and L2
    """

    # equation 18 from the lab 

    z1 = (L1 - L_mean) / stdev 
    z2 = (L2 - L_mean) / stdev 

    # integration limits 
    lims = [z1, z2] 

    return integrate_gauss(standard_normal, lims, npts) 

def main(): 
    
    # values from lab

    mean = 1.5 
    stdev = 0.5 
    mag = 4.0 
    L1 = 10.00 
    L2 = 10.10  
    L_mean = 10.05
    n_list = [1,2,3,4,5] 

    prob_mag_4 = [seismic_prob(mag, mean, stdev, npts) for npts in n_list] 
    print(f'Probability of an earthquake with a magnitude greater than 4.0: {prob_mag_4}') 

    prob_true_value = [probability_length(L1, L2, mean, stdev, npts) for npts in n_list] 
    print(f'probability of a distance between 10.00 and 10.10: {prob_true_value}') 

    # now we will plot teh convergence of  the probility estimates dertmined  using Gauss-Legendre quadrature 
    # for am increasing number of points 
    seismic_probability = [] 
    length_probability = [] 

    for npts in n_list: 
        seismic_probability.append(integrate_gauss(standard_normal, [4, 10], npts)) 
        length_probability.append(integrate_gauss(standard_normal,[((L1 - L_mean) / stdev),  ((L2 - L_mean) / stdev)], npts)) 

    print(f'seismic_probability: {seismic_probability}') 
    print(f'length_probability: {length_probability}') 

    # plot the convergence of the probability for the magnitude of the earthquake 
    plt.figure(figsize=(10, 4))  

    plt.subplot(1, 2, 1) 
    plt.loglog(n_list, seismic_probability, 'o-', label="Seismic Probability") 
    plt.xlabel("Number of points") 
    plt.ylabel("Probability") 
    plt.title("Convergence of Seismic Probability") 
    plt.grid() 
    plt.legend() 

    # plot the convergence of the probability for the length 
    plt.subplot(1, 2, 2) 
    plt.loglog(n_list, length_probability, 'o-', label="Length Probability") 
    plt.xlabel("Number of points") 
    plt.ylabel("Probability") 
    plt.title("Convergence of Length Probability") 
    plt.grid() 
    plt.legend() 

    plt.tight_layout() 
    plt.savefig("figures/Convergence_of_Probability.png") 
    plt.show() 

if __name__ == "__main__": 
    main()