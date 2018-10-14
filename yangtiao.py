#三次样条

import numpy as np
import numpy.linalg as nlg
import matplotlib.pyplot as plt
import sympy as py
import math
def get_h(n,x_set=[]):
    set_save_h=[]
    for i in range(n-1):
        h=x_set[i+1]-x_set[i]
        set_save_h.append(h)
    return set_save_h

def get_M(f_0,f_n,n,x_set=[],y_set=[],h=[]):
    set_save_miu=[]
    set_save_lambda=[]
    set_save_d=[]
    set_save_f=[]
    
    for i in range(n-1):
        f=(y_set[i+1]-y_set[i])/h[i]
        set_save_f.append(f)
        
    d0=6*(set_save_f[0]-f_0)/h[0]
    set_save_d.append(d0)
    
    for j in range(1,n-1):
        miu=h[j-1]/(h[j-1]+h[j])
        lambdai=h[j]/(h[j-1]+h[j])
        d=6*(set_save_f[j]-set_save_f[j-1])/(h[j]+h[j-1])
        set_save_miu.append(miu)
        set_save_lambda.append(lambdai)
        set_save_d.append(d)
        
    dn=6*(f_n-set_save_f[n-2])/h[n-2]
    set_save_d.append(dn)
    
    I=np.zeros((n,n))
    I[0,0]=2
    I[0,1]=1
    for m in range(1,n-1):
        for k in range(n-1):
            if (k+1)==m:
                I[m,k]=set_save_miu[m-1]
                I[m,k+1]=2
                I[m,k+2]=set_save_lambda[m-1]
    I[n-1,n-2]=1
    I[n-1,n-1]=2
    print(I)
    I1=nlg.inv(I)
    print(I1)
    M=np.zeros((n,1))
    D=[set_save_d]
    D1=np.transpose(D)
    print(D1)
    M=np.dot(I1,D1)
    print(M)
    return M

def get_s(n,M=[],x_set=[],y_set=[],h=[]):
    def S(Px):
        ff1=0
        for j in range(n-1):
            s_x=M[j]*(x_set[j+1]-Px)**3/(6*h[j])+M[j+1]*(Px-x_set[j])**3/(6*h[j])+(y_set[j]-M[j]*h[j]**2/6)*(x_set[j+1]-Px)/h[j]+(y_set[j+1]-M[j+1]*h[j]**2/6)*(Px-x_set[j])/h[j]
            ff1=ff1+(Px>=x[j] and Px<x[j+1])*s_x
        return ff1
    return S

if __name__ == '__main__':
    x=[i/10 for i in range(-10,10)]
    y=[1/(1+25*p**2) for p in x]
    s1=0.0740
    sn=-0.0740
    u=len(x)
    print(u)
    h=get_h(u,x)
    print(h)
    M=get_M(s1,sn,u,x,y,h)
    print(M)
    SX=get_s(u,M,x,y,h)
   # x=py.symbols('x')
    SX(0.2800)
    print(SX(0.2800))
    x1=[i/100.00 for i in range(-100,100)]
    print(x1)
    
    #x1=[0.26,0.27,0.28,0.3,0.4,0.5,0.6]
    y1=[SX(i) for i in x1]

    plt.figure("spline")
    ax1 = plt.subplot(111)
    plt.sca(ax1)
    plt.plot(x, y, linestyle = ' ', marker='o', color='b')
    plt.plot(x1, y1, linestyle = '-', color='r')
    plt.show()

xx=np.zeros(6)
y2=np.zeros(6)
y3=np.zeros(6)
def fun(x):
    return 1/(1+25*x*x)

for i in range(1,6):
    xx[i]=-1+math.pi/12*i
    y2[i]=SX(xx[i])
    y3[i]=fun(xx[i])


