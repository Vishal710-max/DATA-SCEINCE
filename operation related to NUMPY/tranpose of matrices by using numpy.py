from numpy import*
r=int (input("enter the no. of rows :"))
c=int (input("enter the no. of columns :"))
n =input ("enter matrix elements :\n")
x=reshape (matrix (n),(r,c))
print ("the origenal matrix is :")
print (x)
print ("transpose of matrix is :")
y=x.transpose ()
print (y)

# import numpy as np
# a=np.array([1, 2, 2, 3, 4, 4, 4, 5, 6])
# uni_val, cnt= np.unique(a, return_counts=True)
# print("Unique values:", uni_val)
# print("Counts of unique values:", cnt)