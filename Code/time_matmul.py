import numpy as np
import matplotlib.pyplot as plt
from LUP_decomposition import LUP
from time import time

nStart = 4
nEnd = 500
table=np.empty((nEnd-nStart,2))
for n in range(nStart, nEnd):
    A=np.random.rand(n,n)
    start=time()
    L,U,P,success=LUP(A)
    stop=time()
    table[n-nStart,:]=[n,stop-start]
plt.loglog(table[:,0],table[:,1],'-*')
plt.loglog(table[:,0],1e-5*table[:,0]**3,'-k')
plt.loglog(table[:,0],1e-5*table[:,0]**2,'-g')

plt.show()