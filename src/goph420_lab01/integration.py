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

    

    def trapezoid(x, f,):  
        """uses trapezoid rule to integrate a function  
        
        Parameters 
        ---------- 
        x : array_like 
            The points at which the function is evaluated.
        f : array_like 
            The function values at the points x.
        
        Returns 
        ------- 
        
        float 
         
        Raises 
        ------ 
        ValueError 
            If x and f do not have the same length.

        Notes 
        ----- 
        Assumes constant step size in the x array.
        
        """
        x = np.array(x).flatten() 
        f = np.array(f).flatten() 
        if len(x) != len(f): 
            raise ValueError("x and f must have the same length") 
        dx = x[1] - x[0]  # Step size  

        integral_trap = 0.5 * dx * (f[0] + 2 * np.sum(f[1:-1]) + f[-1])  # Multi-Application Trapezoid rule
        
        return integral_trap 
    
    def simpson(x, f): 
        """uses Simpson's rule to integrate a function 
        Parameters
        ----------
        x : array_like 
            The points at which the function is evaluated. 
        f : array_like 
            The function values at the points x. 

        Returns 
        ------- 
        float 

        Notes 
        ----- 
        Assumes constant step size in the x array.
        """ 
       
        x = np.array(x).flatten()   
        f = np.array(f).flatten()   
        dx = x[1] - x[0]  # Step size 
        
        integral_simp = dx[0] / 3 * (f[0] + f[-1])  # First and last points 
        integral_simp += np.sum(4 * dx[0] * f[1:-1:2])  # Odd points 
        integral_simp += np.sum(2 * dx[0] * f[2:-1:2]) # Even points  

        return integral_simp


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



