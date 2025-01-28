from __init__ import * 


def integrate_newton(x, f, alg): 
    """
    Integrate a function using Newton-Cotes quadrature. 
    
    Parameters
    ----------
    x : array_like
        The points at which the function is evaluated. 
    f : array_like
        The function values at the points x. 
    alg : str
        The algorithm to use. 
        
    Returns
    -------
    float
        The integral of the function. 
    """ 
    def trapezoid(x, f): 
        """uses trapezoid rule to integrate a function""" 
        


    if alg == 'midpoint': 
        return midpoint(x, f)
    elif alg == 'trapezoid': 
        return trapezoid(x, f)
    elif alg == 'simpson': 
        return simpson(x, f)
    else: 
        raise ValueError("Invalid algorithm. Must be 'midpoint', 'trapezoid', or 'simpson'.")   