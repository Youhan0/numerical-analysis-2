#N_main.py

X=[0.4,0.55,0.65,0.80,0.95,1.05];
Y=[0.41075	,0.57815,0.69675,0.90,1.00,1.25382];

x=float(input("输入x的值："));
#x=0.596;
#print(newton(X,Y));
print(NewtonInterp(X,Y));