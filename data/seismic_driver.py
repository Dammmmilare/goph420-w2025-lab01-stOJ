import numpy as np 
import matplotlib.pyplot as plt 

def main(): 
    # Load the data
    data = np.loadtxt('data/s_wave_data.txt')
    t_data = data[:, 0] 
    v_data = data[:, 1] 
    v2_data = v_data ** 2

    # Plot the data
    plt.figure()  

    plt.subplot(2, 1, 1)
    plt.plot(t_data, v_data, "-b", label='s_wave_data') 
    plt.xlabel("Time [s]") 
    plt.ylabel("Velocity [m/s]") 
    plt.title("S Wave Data") 
    plt.legend() 
    
    plt.subplot(2, 1, 2) 
    plt.plot(t_data, v2_data, "-r", label='s_wave_data') 
    plt.xlabel("Time [s]") 
    plt.ylabel("Velocity Squared [m/s^2]") 
    plt.legend() 
    
    plt.savefig("figures/s_wave_data.png") 
    plt.show() 

if __name__ == "__main__": 
    main()