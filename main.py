import numpy as np
import matplotlib.pyplot as plt
import rys
import gen
from alokacja import *
from funBaz import *
import scipy.integrate as spint
from aij import *
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

n1 = np.shape(wezly)[0]
#warunki brzegowe
# twb_L = 'D'
# twb_P = 'D'

# wwb_L = 0
# wwb_P = 1
# x_a=0
# x_b=1
# n=5
w,e =gen.genTabGeom(x_a,x_b,n)
rys.rysGeom(w,e)

WB = [{"ind":1, "typ": 'D', "wartosc":1},
{"ind":n, "typ": 'D', "wartosc":2}]

A, b = alokacja(n1)

stop_fun_baz =1 
phi,dphi = FunkcjeBazowe(stop_fun_baz)

xx = np.linspace(-1,1,101)
plt.plot(xx,phi[0](xx),'r')
plt.plot(xx,phi[1](xx),'g')
plt.plot(xx,dphi[0](xx),'b')
plt.plot(xx,dphi[1](xx),'c')

#liczba wierszy = liczba elementow
for ee  in np.arange(0,np.shape(elementy)[0]):
    
    elemRowInd = ee
    elemGlobalInd = elementy[ee,0]
    elemWezel1 = elementy[ee,1]
    elemWezel2 = elementy[ee,2]    
    
    Ml = np.zeros([stop_fun_baz+1, stop_fun_baz+1])
    x_a= wezly[elemWezel1-1,1]
    x_b= wezly[elemWezel2-1,1]

    J= (x_b-x_a)/2
    
    m= 0; n =0;
    Ml[m,n] = spint.quad(J*aij(dphi[m], dphi[n], c , phi[m],phi[n]),-1,1)
    m=0; n=1;
    Ml[m,n] = spint.quad(J*aij(dphi[m], dphi[n], c , phi[m],phi[n]),-1,1)
    m=1; n=0;
    Ml[m,n] = spint.quad(J*aij(dphi[m], dphi[n], c , phi[m],phi[n]),-1,1)
    m=1; n=1;
    Ml[m,n] = spint.quad(J*aij(dphi[m], dphi[n], c , phi[m],phi[n]),-1,1)
    print(Ml)
    