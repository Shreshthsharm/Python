import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt
mydata=np.arange(0,15)
dataframe=pd.DataFrame(data=mydata.reshape(3,5))
print(dataframe)
print(dataframe.iloc [1:5,2:5])

mydata=np.arange(0,15)
dataframe=pd.DataFrame(data=mydata.reshape(3,5))
print(dataframe)
print(dataframe.iloc [1:5,1:5])
dataframe.to_json("sample.json")

plt.pie(mydata)
plt.show()