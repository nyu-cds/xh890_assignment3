# -----------------------------------------------------------------------------
# calculator.py
# Before: 1015872 function calls (1015751 primitive calls) in 2.233 seconds
# After: 11860 function calls (11739 primitive calls) in 0.229 seconds
# Speedup = 2.233 / 0.229 = 9.751092
# ----------------------------------------------------------------------------- 

import numpy as np

def hypotenuse(x,y):
    """
    Return sqrt(x**2 + y**2) for two arrays, a and b.
    x and y must be two-dimensional arrays of the same shape.
    """
    xx = np.multiply(x,x)
    yy = np.multiply(y,y)
    zz = np.add(xx, yy)
    return np.sqrt(zz)