
"""
Input: A nxn array of floats
for j from 1 to n-1
    for i from j+1 to n
        m = A[i][j]/A[j][j]
        for k from j to n
            A[i][k] = A[i][k] - m*A[j][k]
        A[i][j] = 0
return A
Output: A nxn array of floats

"""
import numpy as np
small=1e-14

def swap(B,a,b):
    temp=np.copy(B[a-1,:])
    B[a-1,:]=np.copy(B[b-1,:])
    B[b-1,:]=np.copy(temp)
    return B

# In: n X (n+1) array of floats. Note: written so that i and j are indices 1-n and 1-n+1
def Gauss(A):
    B=np.copy(A)
    n=np.shape(A)[0]
    for j in range(1,n):
        #Select the best pivot element: 
        p=np.argmax(abs(B[j-1,j:]))+j
        B=swap(B,j,p)
        if B[j-1][j-1]<small:
            print("Warning: small pivot!")
            return
        for i in range(j+1,n+1):
            m = B[i-1][j-1]/B[j-1][j-1]
            B[i-1,:]=B[i-1,:]-m*B[j-1,:]
    return B

A=np.array([[2,2,-0.5,2],[2,3,2,-2],[2,1,0,4]])
B=Gauss(A)
print(B)