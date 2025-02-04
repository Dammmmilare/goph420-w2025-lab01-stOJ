import numpy as np
from goph420_lab01.integration import ( 
    trapezoid, 
    simpson, 
    integrate_gauss
) 

def test_trapezoid(): 
    x = np.linspace(-2.0, 5.0) 
    f0 = 5.0 * np.ones_like(x) 
    f1 = -2.5 +0.6 * x
    
    I0_exp = f0[0] * (x[1] - x[0]) 
    I0_act_2 = trapezoid( 
          [x[0], x[-1]], 
          [f0[0], f0[-1]],
    ) 

    I0_act_all = trapezoid(x, f0)
    print('testing trapezoid rule')  
    print(f'f(x) = {f0[0]} from x={x[0]} to x={x[1]}') 
    print(f'Expected: {I0_exp}') 
    print(f'Actual: {I0_act_2}') 
    print(f'Acttual all: {I0_act_all}')   
if __name__ == "__main__": 
        test_trapezoid()