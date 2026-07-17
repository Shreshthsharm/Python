import numpy as np
a=np.array([1,2,np.inf,4,-np.inf,6])
print(np.isinf(a))
b=np.nan_to_num(a,posinf=1000,neginf=100)
print(b)