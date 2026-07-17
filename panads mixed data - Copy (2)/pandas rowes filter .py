import pandas as pd 
data={
    "Name":['Shreshth','Kajal','Aman','Ram','Sita','Radha','Krishn','Ganesh'],
    "Age":[23,21,22,28,26,24,25,20],
    "salary":[5000000,550000,558000,650000,6800000,220000,240000,260000],
    "performance":[88,85,86,95,96,94,93,92]
}
df=pd.DataFrame(data)
highe_salary=df[df['salary']>500000]
print("Employee with salary >500000")
print(highe_salary)
fil=df[(df['performance']>90)&(df['salary']>500000)]
print("emplye performance with> 90 + salary with>500000")
print(fil)
# using OR condition
fil_or=df[(df['performance']>90)|(df['Age']>25)]
print("Employee performance or age")
print(fil_or)