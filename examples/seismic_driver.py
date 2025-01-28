import numpy as np 
import matplotlib.pyplot as plt 

def main(): 
    # Load the data
    data = np.loadtxt('examples/s_wave_data.txt')
    t_data = data[:, 0] 
    v_data = data[:, 1]

    # Plot the data
    plt.figure() 
    plt.plot(t_data, v_data, "-b", label='s_wave_data') 
    plt.xlabel("Time [s]") 
    plt.ylabel("Velocity [m/s]") 
    plt.title("S Wave Data") 
    plt.legend() 
    plt.savefig("examples/s_wave_data.png") 
    plt.show() 

if __name__ == "__main__": 
    main()