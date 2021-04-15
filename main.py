import numpy as np
import matplotlib.pyplot as plt
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


def generujTabliceGeometrii(x_0, x_p, n):
    x= np.linspace(x_0, x_p, n+1)
    wez= np.array([[1, x[0]]])
    elem = np.array([[1, 1 ,2 ]] )
    for i in range(1,len(x)):
        wez=np.insert(wez,i,[i+1, x[i]],0)
        elem=np.insert(elem,i,[i+1,i+1,i+2],0)
    elem = np.delete(elem, len(elem)-1,0)
    return np.round(wez,5) ,np.round(elem,5)


def rysujGeom(wezly,elementy):
    obliczwez = np.size(wezly)/2
    print(obliczwez)
    y = np.zeros((int(obliczwez),1))
    plt.plot(wezly[:,1],y,'r.')
    


