import numpy as np
import matplotlib.pyplot as plt
from bis_1 import bis

def normal(x,mu,sig):
    return np.exp(-(x-mu)**2/(2.0*sig**2))/np.sqrt(2.0*np.pi*sig**2)

def errf(x,mu,sig):
    # Using Simpson's rule on M subdomains
    M = 8
    L = mu - 5.0 * sig
    h = (x-L)/float(M)
    I = 0.0
    for i in range(M):
        left = L + float(i)*h
        right = L + float(i+1)*h
        middle = (left+right)/2.0
        I += (normal(left,mu,sig)+4*normal(middle,mu,sig)+normal(right,mu,sig))

    I*=h/6.0
    return I


mu=65.0
sig=25.0
xs=np.linspace(0,100,200)
ys1=[normal(z,mu,sig) for z in xs]
ys2=[errf(z,mu,sig) for z in xs]
plt.plot(xs,ys1,'-k')
plt.plot(xs,ys2,'-r')
plt.show()
# Try to find mu such that the fail fraction is 0.18
targetFail=0.18
def g(z):
    return errf(50,z,sig)-targetFail

xs=np.linspace(-100,100,500)
ys=[g(z) for z in xs]
plt.plot(xs,ys,'-k')
plt.show()
l=50.0
r=100.0
eps_x=1e-7
eps_f=1e-7
kMax=80
muTarget,err,res,conv=bis(g,l,r,eps_x,eps_f,kMax)
if conv:
    print("Target mu=%e." % (muTarget))
else:
    print("Did not converge.")