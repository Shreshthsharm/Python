import pandas as pd 
a=pd.read_csv("basic-data.csv",encoding="latin1")
print("display 10 rowes of first")
print(a.head(10))
print("display 10 rows of last")
print(a.tail(10))
