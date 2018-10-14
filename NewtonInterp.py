#Newton and diffquot

import numpy as np
import sympy as sy

def DiffQuot(X,Y):
      n=len(X);
      D=np.zeros((n,n))
      D[:,0]=Y
      for j in range(1,n):
           for i in range(n-j):
                D[i,j]=(D[i+1,j-1]-D[i,j-1])/(X[i+j]-X[i])
      return D

print()
x=sy.Symbol("x")
def NewtonInterp(X,Y):
      D=DiffQuot(X,Y)
      print('The table of Newton different quotients')
      print(D)
      print()
      n=len(X)-1
      Nn=0
      for k in range(0,n+1):
            t=1
            for j in range(0,k):
                 t=(x-X[j])*t
            Nn=t*D[0,k]+Nn
            print(k,'th Newton interpolation basis function is w',k,'(x)=',t)
            print()
      return Nn