#Sorting and ranking in pandas

# Sorting by columns 
# To sort a pandas DataFrame by a specific column, we can use 
# the sort_values() method.

# Syntax 
# sorted_df = df.sort_values(by='column_name', ascending=flag)

import pandas as pd 
data = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'David'], 
 'Age': [25, 50, 35, 48], 
 'Salary': [10000, 96000, 54000, 52000]}) 
sorted_data = data.sort_values(by='Age', ascending=True) 
print(sorted_data)

# Sorting by rows 
# To sort the rows of a DataFrame based on their index or row 
# labels, we can use the sort_index() method.

# Syntax
# sorted_df = df.sort_index(axis=0, ascending=flag)

import pandas as pd 
data = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'David'], 
 'Age': [25, 50, 35, 48], 
 'Salary': [10000, 96000, 54000, 52000]}) 
sorted_data = data.sort_index(axis=0, ascending=True) 
print(sorted_data)

# Sorting by multiple columns 
# Sorting by multiple columns creates a hierarchical sorting order.

# Syntax

# sorted_df = df.sort_values(by=['column1', 'column2'], 
# ascending=[flag_one, flag_two]) 

import pandas as pd 
data = pd.DataFrame({'Name': ['Alice', 'Bob', 'Alice', 'David'], 
 'Age': [25, 50, 35, 48], 
 'Salary': [10000, 96000, 54000, 52000]}) 
sorted_data = data.sort_values(by=['Name', 'Salary'], 
ascending=[True, False]) 
print(sorted_data)

# Ranking 
# Ranking is assigning ranks or positions to data elements based on their values.
# This is particularly valuable when analyzing data with repetitive 
# values or when you need to identify the top or bottom entries. 

# Syntax
# df['Rank'] = df['column'].rank(axis=0, method='average') 
# The parameters involved are as follows: 
#  axis: Axis to rank. 0 for index and 1 for columns.

import pandas as pd 
data = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'David'], 
 'Age': [25, 35, 35, 48], 
 'Salary': [10000, 96000, 54000, 52000]}) 
data['Rank'] = data['Age'].rank(method='average') 
print(data) 

#the reaminging part like mean,median,mode and std is same as like numpy.

# Pandas DataFrame nunique() Method

# Definition 
# The nunique() method returns the number of unique values for 
# each column. 
# By specifying the column axis (axis='columns'), 
# the nunique() method searches column-wise and returns the 
# number of unique values for each row. 

# Syntax
# dataframe.nunique(axis)

import pandas as pd 
data = [[10, 20, 0], [10, 10, 10], [10, 20, 30]]
df = pd.DataFrame(data) 
print(df.nunique()) 

# Python | Pandas Index.value_counts() 
# Pandas Index.value_counts() function returns object containing 
# counts of unique values.

# Syntax: Index.value_counts(normalize=False, sort=True, 
# ascending=False, bins=None, dropna=True) 

import pandas as pd 
# Creating the index 
idx = pd.Index(['Harry', 'Mike', 'Arther', 'Nick', 
 'Harry', 'Arther'], name ='Student') 
# Print the Index 
print(idx) 
# find the count of unique values in the index 
idx.value_counts()

# Read Text Files with Pandas:

# Below are the methods by which we can read text files with Pandas: 
# Using read_csv() 
# Using read_table() 

# Read Text Files with Pandas Using read_csv()- 
# There are three parameters we can pass to the read_csv() 
# Syntax: data=pandas.read_csv(‘filename.txt’, sep=’ ‘ , header=None, names=[“Column1” , “Column2”]

import pandas as pd 
# read text file into pandas DataFrame 
df = pd.read_csv("gfg.txt", sep=" ") 
print(df)

# Read Text Files with Pandas Using read_table()

import pandas as pd 
# read text file into pandas DataFrame 
df = pd.read_table("gfg.txt", delimiter=" ") 
# display DataFrame 
print(df)