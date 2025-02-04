from __init__ import * 


def integrate_newton(x, f, alg="trap"): 
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

    if alg.strip().lower() == "trap": 
        return trapezoid(x, f) 
    elif alg.strip().lower() == "simp": 
        return simpson(x, f)

    def midpoint(x, f): 
        """uses midpoint rule to integrate a function""" 
        dx = x[1] - x[0]
        return np.sum(f) * dx
    
    def trapezoid(x, f, dx):  
        """uses trapezoid rule to integrate a function""" 
        integral_trap = 0.5 * dx[0] * (f[0] + f[-1])  # First and last points 
        integral_trap += np.sum(dx[0] * f[1:-1])  # Sum of the middle points 
        
        return integral_trap 
    
    def simpson(x, f, dx): 
        """uses Simpson's rule to integrate a function""" 
        integral_simp = dx[0] / 3 * (f[0] + f[-1])  # First and last points 
        integral_simp += np.sum(4 * dx[0] * f[1:-1:2])  # Odd points 
        integral_simp += np.sum(2 * dx[0] * f[2:-1:2]) # Even points  

        return integral_simp


    if alg == 'midpoint': 
        return midpoint(x, f)
    elif alg == 'trapezoid': 
        return trapezoid(x, f)
    elif alg == 'simpson': 
        return simpson(x, f)
    else: 
        raise ValueError("Invalid algorithm. Must be 'midpoint', 'trapezoid', or 'simpson'.")   


def  integrate_gauss():

    '''
    parameters:
    ==========
    f: function to integrate
    lims: limits of integration
    npts: number of points to use in the integration

    returns:
    =======
        float: the integral of f over the interval lims
    ''' 



