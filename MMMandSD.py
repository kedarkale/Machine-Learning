import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

data = []
data = np.random.randint(1,1000,1000)

print ("mean : ",np.mean(data))
print ("median : ",np.median(data))
print ("mode : ",stats.mode(data))

print("\nS.D. : ",data.std())
print("variance : ",data.var())

plt.hist(data,10)
plt.show()