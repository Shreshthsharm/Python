import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

years =np.array([2005,2006,2007,2008,2011])
grades=np.array([54.05,72,82,92,98])
#show data in graph- line (x,y),pie(x),i
#bar(x,y),scatters(x,y)
plt.plot(years,grades)
plt.show()