import numpy as np

arr=np.array ([1,22,3,48,5,61])
arr1=np.array ([10,20,30,40,50,60])
arr2=np.array ([[12,34,56],[67,89,30]])
arr3=np.array ([[[1,2,3],[4,5,6],[7,8,9]]])

#if we perform the following operations which we applied on 1D that we are also applay in 2D and 3D array
#like we applay mean,sum,argmax,average etc on 1D array same we appaly them into 2D & 3D with axis=0 & axis=1
#some arhithematic operation on array :

print ("after adding 5 array become :",arr1+5)
print ("after substraction 5 array become :",arr1-5)
print ("after multiplication 5 array become :",arr1*5)
print ("after division 5 array become :",arr1/5)
print ("after modulation 5 array become :",arr1%5)

#some mathamatical functions :

print("sin values :",np.sin(arr1))
print("cos values :",np.cos(arr1))
print("tan values :",np.tan(arr1))

print("biggest elements :",np.max(arr1))
print("smallset value :",min(arr1))
print ("indearr1 of smallest element :",np.argmin(arr1))
print ("indearr1 of largest  element :",np.argmax(arr1))

print("average of all elements :",np.mean(arr1))
print("SUM of all elements :",sum(arr1))
print("median value of all elements :",np.median(arr1))
print("variance of all elements :",np.var(arr1))
v1=np.std(arr1)
print ("STANDARD DEVATION OF AN ARRAY :",v1)

a=np.sort (arr1)
print ("array in ASCENDING order :",a)
v=arr1.sort(reverse=True)
print ("array in  DESCENDING order :",arr1)

print ("square of each element :",np.power(arr1,2))
print ("square root of each element :",np.sqrt(arr1))
y=[1,2,3,4]
print (y)
print ("product of each element :",np.prod(y))
print ("absoulate value of each element :",abs(arr1))
print ("earr1ponital values of each element :",np.exp(arr1))

#some arithematic operations appiled on 2D and 3D array

print (sum (arr2)) #ans=[ 79 123  86]
print (sum(arr3))#whole array can printed
print (np.sum (arr3))#45

#axis=0 means along to the column
#axis=1 means along to the row

print ("maximum ele. with axis=0",np.max(arr1,axis=0)) #a array whose dimenasion is 1 that are not the optaion of axis=1

print ("maximum ele. with axis=0",np.max(arr2,axis=0)) #create an one vartical line and then compare the array's to each other
print ("maximum ele. with axis=1",np.max(arr2,axis=1))

print ("maximum ele. with axis=0",np.max(arr3,axis=0))
print ("maximum ele. with axis=1",np.max(arr3,axis=1))

# MAXIMUM () 'IT CAN COMPARE THE 2 ARRAY'S TO EACH OTHER AND RETUNR THE LARGER NO. IN 3RD ARRAY'
print ("maximum ele. from both array:",np.max(arr1,arr)) #reambemr the thing we can find the larger no. from 2 array only when both havingsame size
#same like 1D it applicable one 2D or 3D

#numpy array comparison operator 
print ("Grater than :",np.greater (arr,arr1)) #1:condation is same like maximum 2:it will compare to array and return the result in Boolan form like
#Grater than : [False  True False  True False  True]

print ("Grater than or equal to :",np.greater_equal (arr,arr1))
print ("less than :",np.less (arr,arr1))
print ("less than or equal to:",np.less_equal (arr,arr1))
print ("equal to :",np.equal (arr,arr1))
print ("not equal to :",np.not_equal (arr,arr1))
#same like 1D it applicable one 2D or 3D array