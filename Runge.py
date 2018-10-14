# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 17:37:17 2018

@author: lenovo
"""

import matplotlib.pyplot as plt
import numpy as np
import sympy as sy #符号表达
x=sy.Symbol('x')

def Lagrange(X,Y):
    Ln=0.0
    for i in range(len(X)):
        t=1
        for j in range(len(X)):
            if i!=j:
                t*=(x-X[j])/(X[i]-X[j])
        Ln+=t*Y[i]
    print()
    return Ln

def fun(x):
    return 1/(1+25*x*x)

#输入节点与对应函数值
n=10
a=-1
b=1
h=(b-a)/n
X=np.zeros(n+1)
Y=np.zeros(n+1)
for i in range(n+1):
    X[i]=a+i*h
    Y[i]=fun(X[i])
Ln=Lagrange(X,Y)
print('Ln=',Ln)
#画图
xx=np.linspace(-1,1,101)
yy=np.zeros(101)
y=fun(xx)
for i in range(101):
    yy[i]=Ln.subs(x,float(-1+i*0.02))
plt.plot(xx,yy)
plt.plot(xx,y)