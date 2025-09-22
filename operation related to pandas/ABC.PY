import pandas as pd
# making data frame from csv file 
data = pd.read_csv(r"E:\practice\practice for python\DATA SCIENCE\OPERATION RELATED TO PANDAS\abc.csv",index_col='name')
#whole path is needed and there is must that the both file are at same location 
first=data.ix[[2]]
print (first)
#print (data)
"""import pandas as pd 
# making data frame from csv file 
data = pd.read_csv("nba.csv", index_col ="Name") 
# retrieving row by ix method 
first = data.ix["Avery Bradley"] 
print(first)"""