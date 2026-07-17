import numpy as np
a=input("enter youre prices=")
prices=np.array(a.split(),dtype=int)
dicount=25/100
final_price=prices-(prices*dicount)
print(final_price)