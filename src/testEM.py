import numpy as np
import ChngPntDctTry1
import matplotlib.pyplot as plt
from scipy.stats import norm
from tqdm import  tqdm
import pandas as pd

def auc(m1, std1, m2, std2):

    a = 1 / (2 * std1 ** 2) - 1 / (2 * std2 ** 2)
    b = m2 / (std2 ** 2) - m1 / (std1 ** 2)
    c = m1 ** 2 / (2 * std1 ** 2) - m2 ** 2 / (2 * std2 ** 2) - np.log(std2 / std1)
    result = np.roots([a, b, c])
    if len(result) == 0:
        r = m1
    else:
        r = result[0]
    area = norm.cdf(r, m2, std2) + (1. - norm.cdf(r, m1, std1))
    return area


def generateRndGaussian(seed):
    np.random.seed(seed)
    # randomSplit=np.random.randint(200,800)
    randomSplit=200
    mu1List=[5,10,15,20,25]
    mu2List=[6,11,16,21,26]
    sdList=[1,2,3,4,5,6,7,8,9]

    mu1=float(np.random.choice(mu1List,1))
    mu2=float(np.random.choice(mu2List,1))
    sd1=float(np.random.choice(sdList,1))
    sd2=float(np.random.choice(sdList,1))

    arr1= np.random.normal(mu1, sd1, randomSplit)
    arr2= np.random.normal(mu2, sd2, 1000-randomSplit)


    if mu1>mu2:
        mu1,mu2= mu2,mu1
        sd1,sd2= sd2,sd1

    area=z(mu1, sd1, mu2, sd2)
    return [np.append(arr1, arr2), randomSplit, area]



def z(mu1, sd1, mu2, sd2):
    return abs(mu1-mu2)/(np.sqrt(sd1**2+sd2**2))


def simulate(seed=23, trails=100):
    x=[]
    error=[]
    for i in tqdm(range(trails)):
        rndData=generateRndGaussian(seed+i)
        test=ChngPntDctTry1.EM(rndData[0])[0]
        error.append(test-rndData[1])
        x.append(rndData[2])
        print x[i-1],error[i-1]
    return pd.DataFrame({'z': x, 'error':error}).sort('z')

if __name__ == '__main__':
    rnd=simulate()
    rnd.to_csv('/Users/Pagliacci/Desktop/simu2.csv')
    rnd.plot(x= 'z', y='error')
    plt.show()