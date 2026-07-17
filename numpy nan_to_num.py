import numpy as np
a=np.array([1,2,np.nan,4,np.nan,6])
b=np.nan_to_num(a,nan=100)
print(b)