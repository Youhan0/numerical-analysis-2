#LagranInterp.py

import sympy as sy
x=sy.Symbol("x")
def LangranInterp(X,Y):
    L=0;
    n=len(X);
    for j in range(n):
        t=1;
        for k in range(n):
            if k!=j:
                t=t*(x-X[k])/(X[j]-X[k]);
        L=L+Y[j]*t;
    return(L);
