import pandas as pd
import numpy as np
import scipy.stats
from tqdm import tqdm
import warnings
def readData():
    data=pd.read_csv('/Users/Pagliacci/Desktop/ECE 443/finalProject/data/multiTimeline-2.csv')
    return data['freq'].values


def logGaussianPdf(mu, sigma,x):
    return np.log(scipy.stats.norm(mu, sigma).pdf(x))


def sliceNdice(arr, t, mu1, sigma1, mu2, sigma2):
    # t must be between 1 to len-1
    size=len(arr)
    part1=arr[0:t]
    part2=arr[t: size]

    prob1=[logGaussianPdf(mu1,sigma1,i) for i in part1]
    prob2=[logGaussianPdf(mu2,sigma2,i) for i in part2]

    ret=reduce(lambda x,y: x+y,prob1)+reduce(lambda x,y: x+y,prob2)
    if ret==float('-inf'):
        raise Exception
    return ret


def computeFromLastP(LastP, m1, m2):
    return LastP-m2+m1


def mStep(arr, mu1, sigma1, mu2, sigma2):
    curMax=1
    maxP=curP=sliceNdice(arr, 50, mu1, sigma1, mu2, sigma2)

    for t in range(1, len(arr)-1):
        curX=arr[t]
        p1=logGaussianPdf(mu1,sigma1,curX)
        p2=logGaussianPdf(mu2,sigma2,curX)
        newP=computeFromLastP(curP,p1,p2)
        # print  newP
        if newP>maxP:
            curMax=t
            maxP=newP
        curP=newP
    return curMax


def eStep(arr, t):
    size=len(arr)
    part1=arr[0:t]
    part2=arr[t:size]

    mu1 = np.mean(part1)
    sigma1= np.std(part1)
    mu2 = np.mean(part2)
    sigma2= np.std(part2)
    return [mu1, sigma1, mu2, sigma2]


def EM(arr, init_t= None, max_it=None):
    if init_t==None:
        init_t= int(len(arr)/2)
    if max_it==None:
        max_it=10

    (mu1, sigma1, mu2, sigma2) = eStep(arr, init_t)
    lastT= init_t

    for i in  range(max_it):
        init_t = mStep(arr, mu1, sigma1, mu2, sigma2)
        (mu1, sigma1, mu2, sigma2) = eStep(arr, init_t)
        if lastT== init_t:
            break
        else:
            lastT=init_t
        if i== max_it-1:
            warnings.warn('Max Iteration Reaches')

    return [init_t, mu1, sigma1, mu2, sigma2]



if __name__ == '__main__':
    inData=pd.read_csv('/Users/Pagliacci/Desktop/ECE 443/finalProject/data/ImportValues.csv', index_col=0)
    print EM(inData['Value'], max_it=30)

