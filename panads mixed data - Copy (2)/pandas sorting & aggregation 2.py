import pandas as pd 
data={
    "Name":['Shreshth','Kajal','Aman','shka','kash'],
    "Age":[23,21,22,23,21],
    "city":['Shoulana','Delhi','Parpe','shde','shpa'],
    "salary":[500000,60000,45000,500000,22000]
}
df=pd.DataFrame(data)
grouped=df.groupby(["Age","Name"])["salary"].sum()
print(grouped)
