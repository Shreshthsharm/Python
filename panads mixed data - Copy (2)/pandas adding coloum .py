import pandas as pd 
data={
    "Name":['Shreshth','Kajal','Aman','Ram','Sita','Radha','Krishn','Ganesh'],
    "Age":[23,21,22,28,26,24,25,20],
    "salary":[5000000,250000,258000,450000,500000,220000,240000,260000],
    "performance":[88,85,86,95,96,94,93,92]
}
df=pd.DataFrame(data)
print(df)
#squre brakcets df["coloum_name"]=some_data
df['bonus']=df['salary']*0.1
print(df)