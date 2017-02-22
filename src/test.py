import ChngPntDctTry1
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import testEM
# import statsmodels.api as sm


randomSplit=200
mu1List=[18]
mu2List=[20]
sdList=[np.sqrt(2)]
#


mu1=float(np.random.choice(mu1List,1))
mu2=float(np.random.choice(mu2List,1))
sd1=float(np.random.choice(sdList,1))
sd2=float(np.random.choice(sdList,1))

print testEM.z(mu1,sd1,mu2,sd2)
arr1= np.random.normal(mu1, sd1, 500)
arr2= np.random.normal(mu2, sd2, 500)
arr= np.append(arr1, arr2)
ret= pd.DataFrame({'value':arr})
ret.plot()
plt.show()

#
# # ret.to_csv('/Users/Pagliacci/Desktop/25205.csv')
#
# indata= pd.read_csv('/Users/Pagliacci/Desktop/simu.csv', index_col=0)
# # # print np.log(indata['error']+1)
# #
# # plt.plot(indata['z'], np.log(np.log(indata['error'])),'ro')
#
# print len(indata)
# x = indata['z']
# y = indata['error']
# plt.scatter(x, y)
# axes = plt.gca()
# m, b = np.polyfit(x, y, 1)
# X_plot = np.linspace(axes.get_xlim()[0],axes.get_xlim()[1],100)
# plt.plot(X_plot, m*X_plot + b, '-')
# # plt.plot(X_plot, m*X_plot + b, '-')plt.plot(X_plot, X_plot*results.params[0] + results.params[1])
#
# plt.show()