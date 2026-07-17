import pandas as pd 
data={
    "Name":['Shreshth','Kajal','Aman' ,'shka','kash'],
    "Age":[23,21,22,21,23],
    "city":['Shoulana','Delhi','Parpe','new delhi','shdepa'],
    "salary":[50000,60000,45000,75000,80000]
}
df=pd.DataFrame(data)
grouped=df.groupby("Age")["salary"].sum()
print(grouped)