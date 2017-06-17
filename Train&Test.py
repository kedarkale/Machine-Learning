import numpy as np
from pylab import *
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.metrics import r2_score

pageSpeed = np.random.normal(10,2,1000)
purchaseAmount = np.random.normal(10,2,1000)/pageSpeed

xTrain = pageSpeed[:800]
yTrain = purchaseAmount[:800]

xTest = pageSpeed[800:]
yTest = purchaseAmount[800:]

eq = np.poly1d(np.polyfit(xTrain,yTrain,4))

plt.scatter(xTest,yTest)
plt.scatter(xTest,eq(xTest),c='r')
plt.show()

print("regression : ",r2_score(yTest,eq(xTest)))