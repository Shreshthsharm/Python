import pandas as pd 
data={
    "Name":['Shreshth','Kajal','Aman','Ram','Sita','Radha','Krishn','Ganesh'],
    "Age":[23,21,22,28,26,24,25,20],
    "salary":[5000000,250000,258000,450000,500000,220000,240000,260000],
    "performance":[88,85,86,95,96,94,93,92]
}
df=pd.DataFrame(data)
#display the dataframe
print("sample DataFrame")
print(df)
print("Nmae(single colum return series)")
name=df[['Name','Age','salary']]
print(name)