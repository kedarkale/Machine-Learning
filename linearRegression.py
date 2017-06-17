import numpy as np
from pylab import *
import matplotlib.pyplot as plt
from scipy import stats

y=[]
pageSpeeds = np.random.uniform(3.0, 1, 1000)
purchaseAmount = 100 - (pageSpeeds + np.random.normal(0, 0.1, 1000)) * 3

plt.scatter(pageSpeeds, purchaseAmount)

slope,intercept,r_value,p_value,stderr=stats.linregress(pageSpeeds,purchaseAmount)
print(stats.linregress(pageSpeeds,purchaseAmount))
print("covariance : ",np.cov(pageSpeeds,purchaseAmount))

for i in pageSpeeds:
    y.append(slope*i+intercept)
    
plt.plot(pageSpeeds,y,c='r')    
plt.show()