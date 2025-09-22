from numpy import*
x=[]  #creating an empty array
print("how many elements :",end='')
n=int(input())  #accept input n
for i in range (n):
    print('enter a element ',i+1,":",end='')
    x.append(int(input()))
print ("original array :",x)

#some mathamatical functions :
print("sin values :",sin(x))
print("cos values :",cos(x))
print("tan values :",tan(x))
print("biggest elements :",max(x))
print("smallset value :",min(x))
print("average of all elements :",mean(x))
print("median value of all elements :",median(x))
print("variance of all elements :",var(x))