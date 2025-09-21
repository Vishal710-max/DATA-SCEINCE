import numpy as np
# CREATING array by using diff way's

#1:
arr=np.arange (1,6,1) #create an equally spaced array
print (arr)

#2:
arr1=np.linspace (1,3,5) #create an array by using value of start=1 and stop=3 which contain totally 5 values 
print (arr1)

#3:
arr2=np.zeros ((2,3),dtype=int) #create an specified array which contain only zeroes 
print (arr2)

#4:
arr3=np.ones ((2,3),dtype='int')#create an specified array which contain only ones
print (arr3)

#5:
arr4=np.empty ((2,3),dtype='float') #create an array having specific shape and dtype
print (arr4)

#6:
arr5=np.array([1,2,3,4,5]) #Normal method
print (arr5)

#7:
arr6=np.eye ((3),dtype='int') #create an identity matrix
print (arr6)

#8:
arr7=np.full ((3,4),5) #create an ARRAY WHICH IS TOTALLY FULL
print (arr7)

#iterating the numpy array by using  nditer ()
for i in np.nditer (arr):
    print (i)

#iterating the multidimenasional array
a=np.array ([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for i in np.nditer (a) :
    print (i)