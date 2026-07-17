import pandas as pd 
data={
    "Name":['Shreshth','Kajal','Aman'],
    "Age":[23,21,22],
    "city":['Shoulana','Delhi','Parpe']
}
df=pd.DataFrame(data)
print(df)
df.sort_values(by="city",ascending=False,inplace=True)
print("assending order of city list")
print(df)