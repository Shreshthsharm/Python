import numpy as np
a=input("value of 1st array :=>")
b=np.array(a.split(),dtype=int)
c=input("value of 2nd array :=>")
d=np.array(c.split(),dtype=int)
r=b+d
print("answer of r :=>",r)
