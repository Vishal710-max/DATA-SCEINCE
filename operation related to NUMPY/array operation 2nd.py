import numpy as np
a=np.array ([[10,20],[30,40]])
b=np.array ([[11,22],[33,44]])
arr=np.array ([1,22,3,48,5,61])
arr1=np.array ([10,20,30,40,50,60])
arr2=np.array ([[12,34,56],[67,89,30]])
arr3=np.array ([[[1,2,3],[4,5,6]],[[6,7,8],[9,4,1]]])

#numpy array maniuplation operations

print (arr) #reshaping 1D array
v=arr.reshape (2,3) #converating into 2 rows and 3 column's
print (v)

v1=arr3.reshape (-1) #one technique to convert 3D to 1D
print (v1)

v2=arr3.flatten () #one inbuilt method to convert 3D to 1D
print (v2)
print (arr3.shape)

#Transposing the array
print (arr)
print ("Transposing the array :",np.transpose(arr2))

#copying the array
v3=np.copy (arr)
print (v3)

#resizing the array 
v5=np.resize (arr2,(3,3))

#combining stacking and splittig the arrays

#axis=0  represent the vartical concationation 
#axis=1  represent the Horizontial concationation

v6=np.concatenate ((a,b),axis=0)
print (v6)

v7=np.concatenate ((a,b),axis=1)
print (v7)

v8=np.stack ((a,b),axis=0)
print (v8)

v9=np.hstack ((a,b)) #[[10 20 11 22]
print (v9)           #[30 40 33 44]]
 

v9=np.vstack ((a,b))
print (v9) #[[10 20] 
            #[30 40] 
            #[11 22] 
            #[33 44]]