import numpy as np
print ("current version of numpy :",np.__version__) #checking the version of numpy

arr=np.array ([1,3,6,9,10])
print (arr)
print (type(arr)) #type function can show the type of object pased to function

arr0=np.array (43)
print (arr0.ndim)#checking the dimension of an array

arr1=np.array ([1,2,3,4,5,6])
print (arr1.ndim)

arr2=np.array ([[12,34,56],[67,89,30]])
print (arr2.ndim)

arr3=np.array ([[[1,2,3],[4,5,6]],[[6,7,8],[9,4,1]]])
print (arr3.ndim)

#creating the higher dimension array

arr5=np.array ([1,2,3,4],ndmin=5)
print ("dimension of array:",arr5.ndim)

#indexing and slicing
print (arr1[1] + arr1[2])
print (arr2[0]+arr2[1])
print (arr3[0])
print (arr3[1])

#accessing and indexing the 2D and 3D array elements
print (arr2[0,1]) #ans=6 here '0' indicate the index of 2D array and '1' is indicate the inner index of array ele.
print (arr3[0,1,2])#ans=6 

# Negative Indexing 
print (arr1[-1])
print (arr2[1,-1])#same processer like above ex. but in negative side  

#slicing the ndarray

# 1D ARRAY
print (arr[3:]) #o/p [9,10,90,8]         
print (arr[:3]) #o/p [1,3,6]
print (arr[1:7:2])#ANS =[ 3  9 90]
print (arr1[-3:-1]) #ans=[10 90]
print (arr1[-5:-2]) #ans=[ 6  9 10]

#   2D ARRAY
print (arr2[1,1:2]) #First 1 is indicate index of 2D array 
#then we applay slicing method similar like 1D
print (arr2[0:2,0])#[10 40]
print (arr2[0:2,1])#[20 50]
print (arr2[0:2,1:3])#[[20 30] 
                     #[50 60]]

#3D array
print(arr3[0:2,1:4]) 
print (arr3[0:2:1])  # all working is same like 1D and 2D array