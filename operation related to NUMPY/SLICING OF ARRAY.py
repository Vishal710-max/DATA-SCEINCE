from numpy import *
import numpy as np
#1-D array:
a=arange (1,6)
print (a)
s=np.array([0,1,2,3,4,5,6,7,8])
print (s[:4])
print (s[-4:-2])
print (s[-6:-3])
print (s[1:4:2])

#2-D array:
s1=np.array([[1,2,3,4],[5,6,7,8]])
print (s1[:2])
print (s1[1:2,3])
print (s1[0,-4])  #-4 is the index pos. of element where 0 is the pos. inside that element  
print (s1[:2,3])  #this type of slicing can show the o/p in the form of index 
print (s1[0,3])   #like 0=is positon of element in givin array & 3=is the inside pos. of element

#3-D array:   
s2=np.array ([[[1,2,3],[4,5,6],[7,8,9]]])
print (s2)
print (s2[:1,2])

print (s.ndim)
print (s1.ndim)
print (s2.ndim)
print (s.shape)  #it can show the total count of element in array :
print (s.itemsize)#it can show the memory size of element in array according to datatype like 'int'
print (a.itemsize) #float =8