import numpy as np
from scipy import stats as st

# mean = average value
# median = middle value if data is arranged
# mode = most repeated value

dataset = [50,60,55,80,70,95]
print(np.mean(dataset))

salary = [65000 , 85000 , 90000 , 70000 , 80000 , 65000]
print(np.mean(salary))
print(np.max(salary))
print(np.min(salary))
print(np.median(salary))
print(st.mode(salary))