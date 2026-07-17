# prediction:- regression:- it is a relaiton between variables or dataset
# linear regression:- y=mx+c
import matplotlib.pyplot as plt
from scipy import stats as st
age = [20,25,45,30,50,40]
salary = [20000,25000,45000,30000,50000,40000]
plt.plot(age,salary)
slope,intercept,r,p,std_err=st.linregress(age,salary)
print("slope",slope , "intercept",intercept , "r",r , "p",p , "std_err",std_err)
# note:- if r is near to 1 , so best case
# note:- if r is near to 0 , so bad case
plt.show()
from sklearn.metrics import r2_sore
import numpy as np
futuredata=np.polyld(np.ployfit(age,salry,30))