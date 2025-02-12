import numpy as np 


def integrate_newton(x, f, alg="trap"):  
    
    """
    Integrate a function using Newton-Cotes quadrature. 
    
    Parameters
    ----------
    x : array_like
        The points at which the function is evaluated. 
    f : array_like
        The function values at the points x. 
    alg : str, optional
        The algorithm to use 'trap' as trapezoid and 'simp' as simpson's. 
        
    Returns
    -------
    float
        The integral of the function.  

    """  
    x = np.asarray(x)
    f = np.asarray(f)

    if x.shape  != f.shape:
        raise ValueError("x and f must have the same shape")
    
    dx = np.diff(x)
    if not np.allclose(dx, dx[0]):
        raise ValueError("x must be equally spaced")
    
    if alg.lower().strip() == "trap":
        return np.trapz(f, x)
    
    elif alg.lower().strip() == "simp":
        if len(x) % 2 == 0:
            raise ValueError("Simpson's rule requires an odd number of points")
        return np.sum((f[0:-1:2] + 4*f[1::2] + f[2::2]) * (dx[0] / 3))

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
        
        integral_simp = (f[0] + f[-1])  # First and last points 
        integral_simp += np.sum(4 * f[1:-1:2])  # Odd points 
        integral_simp += np.sum(2 * f[2:-1:2]) # Even points  
        integral_simp *= dx / 3
        return integral_simp

    if alg.strip().lower() == "trap": 
        return trapezoid(x, f) 
    elif alg.strip().lower() == "simp": 
        return simpson(x, f)

def integrate_gauss(f, lims, npts):
    """
    This function performs numerical integration of a function using Gauss-Legendre quadrature.

    Parameters
    -----
    f: callable object
        Function to be integrated.
    lims: object with len(2).
        Contains the lower and upper bound of integration.
    npts: int
        Has possible values of 1, 2, 3, 4, 5, but a default of 3.

    Returns
    -----
    float: float
        Provides the integral estimate.

    Raises
    -----
    TypeError
        If f is not callable.
    ValueError
        If lims does not have a length of 2.
    ValueError
        If lims[0] or lims[1] are not float convertible.
    ValueError
        If npts is not one of the possible values.
    """

    if not callable(f):
        raise TypeError("The function f must be callable.")
    if not len(lims) != 2:
        raise ValueError("The parameter 'lims' must have two elements: a and b.")
    if lims[0] != float(lims[0]) or lims[1] != float(lims[1]):
        raise ValueError("lims[0] and lims[1] must be float convertible. ")
    if npts not in [1, 2, 3, 4, 5]:
        raise ValueError("npts must be either 1, 2, 3, 4, or 5.")

        # creating sample points and weights for integration over [-1, 1]
    xi_star, ci_star = np.polynomial.legendre.leggauss(npts)
    a, b = lims

        # shifts then scales sample points from [-1, 1] to [a, b], eq (9)
    xi = ((b + a)/2) + (((b - a)/2) * xi_star)

        # only scales weights from [-1, 1] to [a, b], eq (10)
    ci = ((b - a)/2) * ci_star

        # approx integral
    integral = 0
    for i in range(npts):
        integral += ci[i] * f(xi[i])
    
    return integral
    



