import numpy as np
def genTabGeom(x_0, x_1, n):
    x= np.linspace(x_0, x_1, n)
    wez= np.array([[1, x[0]]]) 
    elem = np.array([[0, 0 ,0 ]] ) 
    for i in range(1,len(x)):
        wez=np.insert(wez,i,[i+1, x[i]],0) 
        elem=np.insert(elem,i-1,[i,i,i+1],0) 
    elem = np.delete(elem, len(elem)-1,0)
    return np.round(wez,5) ,np.round(elem,5)
