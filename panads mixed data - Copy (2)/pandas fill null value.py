import pandas as pd 
data={
    "Name":['Shreshth','Kajal','None','Ram','Sita','Radha','Krishn','Ganesh'],
    "Age":[23,21,None,28,26,24,25,20],
    "salary":[5000000,250000,None,450000,500000,220000,240000,260000],
    "performance":[88,85,None,95,96,94,93,92]
}
df=pd.DataFrame(data)
print(df)
#default value bharne kailye null mai
#df.fillna(0,inplace=True)
#default value ki jgh koi calculator value bharni ho to
#==
#df['Age']=pd.to_numeric(df['Age'],errors='coerce')
df['Age']=df['Age'].fillna(df['Age'].mean(),inplace=True)
df['salary']=df['salary'].fillna(df['salary'].mean(),inplace=True)
print(df)