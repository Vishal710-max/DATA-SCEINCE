import pandas as pd
print (pd.__version__)

#PANDAS SERIES
#A Pandas Series is like a column in a table. 
#It is a one-dimensional array holding data of any type.
a1=[1,4,6]
print (pd.Series(a1))

#Lables
b=[2,4,8]
v=pd.Series (b)
print (v[0])

#by using the index
a = [1, 7, 2] 
myvar = pd.Series(a, index = ["First", "Second", "Third"])
print(myvar["SECOND"]) 

#BY USING THE DICTIONARY
DATA ={"DAY 1":10000,"DAY 2":20000,"DAY 3":30000}
v=pd.Series (DATA)
print (v)

#pandas Dataframe
# A Pandas DataFrame is a 2 dimensional data structure, like a 2 
# dimensional array, or a table with rows and columns. 
data = { 
 "calories": [420, 380, 390],
 "duration": [50, 40, 45] 
 } 
#load data into a DataFrame object: 
df = pd.DataFrame(data) 
print(df)

df = pd.DataFrame(data)
print (df.loc[0])#display the 1st row 
print(df.loc[[0,1]])#display the 1st and 2nd row

#LOAD A FILE INTO DATAFRAME 
df = pd.read_csv('data.csv') 
print(df)

#droping the entries by using the column:
data = { 
 "name": ["Sally", "Mary", "John"],
 "age": [50, 40, 30],
 "qualified": [True, False, False] 
} 
df = pd.DataFrame(data) 
newdf = df.drop("age", axis='columns') #here "age" is an column in above Dataframe where axis value is 'column'
print(newdf) 

#droping the entries by using the Row:
data = { 
 "name": ["Sally", "Mary", "John"],
 "age": [50, 40, 30],
 "qualified": [True, False, False] 
} 
df = pd.DataFrame(data) 
print (df)
print ("\n")
newdf = df.drop(0, axis='index') #here "age" is an Row in above Dataframe where axis value is 'index'
print (newdf) 

# Apply, Map, ApplyMap -Functions 
# in Pandas

#APPLY ()
# Syntax
# dataframe.apply(func, axis, raw, result_type, args, kwds)

import pandas as pd 
def calc_sum(x): 
 return x.sum()
data = { 
 "x": [50, 40, 30],
 "y": [300, 1112, 42] 
} 
df = pd.DataFrame(data) 
x = df.apply(calc_sum)

# map()- 
# Definition 
# The map() function executes a specified function for each item in an iterable. The item is 
# sent to the function as a parameter. 
# Syntax
# map(function, iterables)

import pandas as pd 
def myfunc(a): 
 return len(a) 
x = map(myfunc, ('apple', 'banana', 'cherry')) 
print(x) 
#convert the map into a list, for readability: 
print(list(x))

# applymap()
# Definition 
# The applymap() method allows you to apply one or more functions to the DataFrame object. 
# Syntax
# dataframe.applymap(func, args, kwargs

import pandas as pd 
def make_big(x): 
 return x.upper() 
data = { 
 "name": ["Sally","Mary","John"],
 "city": ["London", "Tokyo", "Madrid"] 
} 
df = pd.DataFrame(data) 
newdf = df.applymap(make_big) 
print(newdf)