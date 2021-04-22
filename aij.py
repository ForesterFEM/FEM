import numpy as np

def aij(dphi1, dphi2, c, phi1, phi2):
    aij = lambda x: -dphi1(x)*dphi2(x) + c *phi1(x)* phi2(x)
    return aij