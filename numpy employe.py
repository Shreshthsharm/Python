import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt
mydata=np.arange(0,12)
dataframe=pd.DataFrame(data=mydata.reshape(3,4))
print(dataframe)
print(dataframe.iloc [1:3,2:4])

mydata=np.arange(0,12)
dataframe=pd.DataFrame(data=mydata.reshape(3,4))
print(dataframe)
print(dataframe.iloc [1:3,1:3])
dataframe.to_json("sample.json")

plt.pie(mydata)
plt.show()