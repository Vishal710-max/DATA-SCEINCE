#exchange the nba.csv file to E:\practice\practice for python\DATA SCIENCE\OPERATION RELATED TO PANDAS\abc.csv

"""Pandas support four types of Multi-axes indexing they are: 
Dataframe.[ ] ; This function also known as indexing operator 
Dataframe.loc[ ] : This function is used for labels. 
Dataframe.iloc[ ] : This function is used for positions or integer based 
Dataframe.ix[] : This function is used for both label and integer based"""

#simple program to print the data from  .csv file

#import os
#print (os.getcwd ()) it can return the givin path E:\practice\practice for python\DATA SCIENCE

import pandas as pd
# making data frame from csv file 
data = pd.read_csv(r"E:\practice\practice for python\DATA SCIENCE\OPERATION RELATED TO PANDAS\abc.csv")
#whole path is needed and there is must that the both file are at same location 
print(data)

#small splling mistake can create some errors like invalid file\Folder name or any filed name from that file
#Example: Selecting a single columns *******
data = pd.read_csv(r"E:\practice\practice for python\DATA SCIENCE\OPERATION RELATED TO PANDAS\abc.csv",index_col ="name") 
#retrieving columns by indexing operator we can use both 
first = data["age"] 
print(first)

#Example:Selecting multiple columns ********
import pandas as pd 
data = pd.read_csv(r"E:\practice\practice for python\DATA SCIENCE\OPERATION RELATED TO PANDAS\abc.csv", index_col ="Name") 
# retrieving multiple columns by indexing operator 
first = data[["age", "college", "salary"]]#when we can Selecting multiple columns that time we use [[]] this dictionary 
print(first)
  
#Indexing a DataFrame using .loc[ ]
# Example: Selecting a single row 
# In order to select a single row using .loc[] , we put a single row label in a .loc function.

import pandas as pd  
data = pd.read_csv(r"E:\practice\practice for python\DATA SCIENCE\OPERATION RELATED TO PANDAS\abc.csv", index_col ="name") # retrieving row by loc method 
first = data.loc["virat"] 
second = data.loc["rohit"] 
print(first, "\n\n\n", second) 
# As shown in the output image, two series were returned since there was only one parameter both of the times.

# Example:Selecting multiple rows 
# In order to select multiple rows, we put all the row labels in a list and pass that to .loc function. 

import pandas as pd 
data = pd.read_csv(r"E:\practice\practice for python\DATA SCIENCE\OPERATION RELATED TO PANDAS\abc.csv", index_col ="name") 
# retrieving multiple rows by loc method 
first = data.loc[["abd", "msd"]] 
print(first)

# Example:Selecting two rows and three columns 
# In order to select two rows and three columns, we select a two rows which we want 
# to select and three columns and put it in a separate list like this: 
# Dataframe.loc[["row1", "row2"], ["column1", "column2", "column3"]] thes sequance is important if we change the seq. 
# that means interchanging the position of row and column the error will be occur
import pandas as pd  
data = pd.read_csv("nba.csv", index_col ="Name") 
# retrieving two rows and three columns by loc method 
first = data.loc[["Avery Bradley", "R.J. Hunter"], ["Team", "Number", "Position"]] 
print(first)

# Example:Selecting all of the rows and some columns 
# In order to select all of the rows and some columns, we use single colon [:] to select 
# all of rows and list of some columns which we want to select like this: 
# Dataframe.loc[:, ["column1", "column2", "column3"]] 
import pandas as pd 
data = pd.read_csv("nba.csv", index_col ="Name") 
# retrieving all rows and some columns by loc method 
first = data.loc[:, ["Team", "Number", "Position"]] 
print(first)

# Indexing a DataFrame using .iloc[ ] : 
# This function allows us to retrieve rows and columns by position. In order to do that, 
# we’ll need to specify the positions of the rows that we want, and the positions of the columns that we want as well. 
# The df.iloc indexer is very similar to df.loc but only uses integer locations to make its selections. 
# basic diff between the iloc and loc method is in .loc[] method we can pass the row or column name but in .iloc[] we can pass the index value of row or column

# Example:Selecting a single row by using the iloc method
import pandas as pd 
data = pd.read_csv("nba.csv", index_col ="Name") 
# retrieving rows by iloc method 
row2 = data.iloc[3] 
print(row2) 

#Example:Selecting multiple rows 
import pandas as pd 
# making data frame from csv file 
data = pd.read_csv("nba.csv", index_col ="Name") 
# retrieving multiple rows by iloc method 
row2 = data.iloc [[3, 5, 7]] 
print(row2) 

# Example:Selecting two rows and two columns 
# In order to select two rows and two columns, we create a list of 2 integer for rows 
# and list of 2 integer for columns then pass to a .iloc[] function. 
import pandas as pd 
data = pd.read_csv("nba.csv", index_col ="Name") 
# retrieving two rows and two columns by iloc method 
row2 = data.iloc [[3, 4], [1, 2]] 
print(row2) 

#Example:Selecting all the rows and a some columns
import pandas as pd 
# making data frame from csv file
data = pd.read_csv("nba.csv", index_col ="Name") 
# retrieving all rows and some columns by iloc method 
row2 = data.iloc [:, [1, 2]] 
print(row2) 
 
#Indexing a using Dataframe.ix[ ] :
#it is an old version which can perform or not on the current computer
import pandas as pd 
data = pd.read_csv("nba.csv", index_col ="Name") 
# retrieving row by ix method 
first = data.ix["Avery Bradley"] 
print(first)

