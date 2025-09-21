from numpy import*
import numpy as np
#a=arange(10)
a=np.array([12,34,56,78,90,67])
print(a)
a=a.reshape (2,3)  #2->it is a row where 5->it is a coloumn
print (a)
s2=np.array ([[[1,2,3],[4,5,6],[7,8,9]]])
print (s2)
s2=s2.flatten ()
print (s2)