#L_main.py 

'''第1题'''    
X=[0.4,0.55,0.65,0.80,0.95,1.05];
Y=[0.41075	,0.57815,0.69675,0.90,1.00,1.25382];
#x=0.596;
x=float(input("输入x的值："))
print(LangranInterp(X,Y));

'''第2题'''
import numpy as np
import matplotlib.pyplot as plt
X=np.linspace(-1, 1, num=11);
Y=[];
for i in range(11):
    Y.append(1/(1+25*X[i]));
yy=[];
for i in range(11):
    x=X[i];
    yy.append(LangranInterp(X,Y));
plt.plot(X,yy,linestyle = '--', color='r');
