import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
  
data = np.random.normal(10,1,1000)

plt.hist(data,50)
plt.show()

print("mean : ",np.mean(data))
print("variance : ",np.var(data))
print("skew : ",stats.skew(data))
print("kurtosis : ",stats.kurtosis(data))