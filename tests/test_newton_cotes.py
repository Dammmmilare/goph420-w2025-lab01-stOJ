import numpy as np
from goph420_lab01.integration import ( 
    integrate_newton, 
    integrate_gauss,
) 

def test_trapezoid(): 
    x = np.linspace(-2.0, 5.0) 
    f0 = 5.0 * np.ones_like(x) 
    f1 = -2.5 +0.6 * x
    
    I0_exp = f0[0] * (x[1] - x[0]) 
    I0_act_2 = integrate_newton( 
          [x[0], x[-1]], 
          [f0[0], f0[-1]], 
          alg="trap"
    ) 
    I0_act_all = integrate_newton(x, f0, alg="trap") 

    print('testing trapezoid rule')  
    print(f'f(x) = {f0[0]} from x={x[0]} to x={x[1]}') 
    print(f'Expected: {I0_exp}') 
    print(f'Actual: {I0_act_2}') 
    print(f'Acttual all: {I0_act_all}')   
    print(f'Error: {I0_exp - I0_act_2}')

def test_simpson(): 
    x = np.linspace(-2.0, 5.0) 
    f0 = 5.0 * np.ones_like(x) 
    f1 = -2.5 +0.6 * x
    
    I0_exp = f0[0] * (x[1] - x[0]) 
    I0_act_2 = integrate_newton( 
          [x[0], x[-1]], 
          [f0[0], f0[-1]], 
          alg="simp",
    ) 
    I0_act_all = integrate_newton(x, f0, alg="simp") 

    print('testing simpson rule')  
    print(f'f(x) = {f0[0]} from x={x[0]} to x={x[1]}') 
    print(f'Expected: {I0_exp}') 
    print(f'Actual: {I0_act_2}') 
    print(f'Acttual all: {I0_act_all}')   
    print(f'Error: {I0_exp - I0_act_2}')

if __name__ == "__main__": 
        test_trapezoid() 
        test_simpson()