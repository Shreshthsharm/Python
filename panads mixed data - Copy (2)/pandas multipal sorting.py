import pandas as pd 
data={
    "Name":['Shreshth','Kajal','Aman'],
    "Age":[23,21,22],
    "city":['Shoulana','Delhi','Parpe']
}
df=pd.DataFrame(data)
print(df)
df.sort_values(by=["city","Name"],ascending=False,inplace=True)
print("sorted city and Name ascending")
print(df)