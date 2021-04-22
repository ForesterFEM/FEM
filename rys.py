import numpy as np
import matplotlib.pyplot as plt
def rysGeom(wezly,elementy):
    obliczwez = np.size(wezly)/2
    print(obliczwez)
    y = np.zeros((int(obliczwez),1))
    plt.plot(wezly[:,1],y,'b-',wezly[:,1],y,'r.')
    