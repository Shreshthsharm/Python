import pandas as pd 
data={
    "Name":['Shreshth','Kajal','Aman'],
    "Age":[23,21,22],
    "city":['Shoulana','Delhi','Parpe']
}
df=pd.DataFrame(data)
print(df)
df.to_excel("my file 1.xlsx",index=False)