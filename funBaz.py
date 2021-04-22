import numpy as np

def FunkcjeBazowe(n):
    # n- stopien wielomianu bedacy funkcjami bazowymi/ksztaltu
    if n == 0:
        f = (lambda x: 1+ 0*x)
        df =(lambda x: 0*x)
    elif n ==1:
        f = (lambda x: -0.5*x+0.5,lambda x: 0.5 *x+0.5)
        df =(lambda x: -0.5 + 0*x,lambda x: 0.5+ 0*x)
    # elif n==2:
    else:
        raise Exception('Blad w parametrach')
            
    return f,df
    