import numpy as np
import matplotlib.pyplot as plt
import rys
import gen
c=0
f=0
x_0=0
x_p=1
wezly= np.array([[1, 0],
          [2, 1],
          [3, 0.5],
          [4, 0.75]])


elementy= np.array([[1, 1, 3],
                    [2, 4, 2],
                    [3, 3, 4]])


#warunki brzegowe
twb_L = 'D'
twb_P = 'D'

wwb_L = 0
wwb_P = 1

z,c =gen.genTabGeom(0,1,5)
rys.rysGeom(z,c)
    


