import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x*np.sin(x)
def df(x):
    return np.sin(x)+x*np.cos(x)
def lin(x,x0,x1,y0,y1):
    return y0+(x-x0)*(y1-y0)/(x1-x0)

xb=0.2
xs=np.linspace(0,1,1000)
ys=f(xs)
plt.plot(xs,ys,'-')
plt.plot([xb],[f(xb)],'*')
plt.show()

h=0.5
x0=xb
y0=f(xb)
exact = df(xb)
errs=[]

while h>1e-3:
    x1=xb+h
    y1=f(x1)
    ylin=lin(xs,x0,x1,y0,y1)
    plt.plot(xs,ys,'-')
    plt.plot(xs,ylin,'r')
    plt.plot([x0,x0],[0,y0],'--k')
    plt.plot([x1,x1],[0,y1],'--k')
    plt.plot([0,1],[0,0],'-k')
    plt.title('h='+str(h))
    plt.show()
    fd=(y1-y0)/(x1-x0)
    errs.append([h,np.abs(exact-fd)])
    h/=2.0

errs=np.array(errs)
plt.loglog(errs[:,0],errs[:,1],'-k')
plt.loglog(errs[:,0],errs[:,0],'-r')
plt.show()


h=0.2
errs=[]

while h>1e-3:
    x0=xb-h
    y0=f(x0)
    x1=xb+h
    y1=f(x1)
    ylin=lin(xs,x0,x1,y0,y1)
    plt.plot(xs,ys,'-')
    plt.plot(xs,ylin,'r')
    plt.plot([x0,x0],[0,y0],'--k')
    plt.plot([x1,x1],[0,y1],'--k')
    plt.plot([0,1],[0,0],'-k')
    plt.title('h='+str(h))
    plt.show()
    fd=(y1-y0)/(x1-x0)
    errs.append([h,np.abs(exact-fd)])
    h/=2.0

errs=np.array(errs)
plt.loglog(errs[:,0],errs[:,1],'-k')
plt.loglog(errs[:,0],errs[:,0],'-r')
plt.show()