import numpy as np
a=np.array([
    list(map(int,input("row 1:=").split())),
    list(map(int,input("row 2:=").split()))
    ])
b=input("ente vactor value :=")
c=np.array(b.split(),dtype=int)
result=a+c
print("result is :=",result)