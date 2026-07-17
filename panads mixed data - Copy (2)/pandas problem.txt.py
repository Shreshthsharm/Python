#import pandas as pd
#a=pd.read_csv("basic-data.csv",encoding="latin1")
import pandas as pd 
data={
    "Name":['Shreshth','Kajal','Aman'],
    "Age":[23,21,22],
    "city":['Shoulana','Delhi','Parpe']
}
df=pd.DataFrame(data)
print("dispalying the info of dta set")
print(df.info())

