import numpy as np



def zeroMean(dataMat):
    meanVal=np.mean(dataMat,axis=0)
    newData=dataMat-meanVal
    return newData,meanVal
def PCA(dataMat,n):
    newData,meanVal=zeroMean(dataMat)
    covMat=np.cov(newData,rowvar=0)
    eigVals,eigVects=np.lina.eig(np.mat(covMat))
    eigValIndice=np.arg.sort(eigVals)
    n_eigValIndice=eigValIndice[-1:-(n+1):-1]
    n_eigVect=eigVects[:,n_eigValIndice]
    lowDataMat=newData*n_eigVect
    reconMat=(lowDataMat*n_eigValIndice.T)+meanVal
    return lowDataMat,reconMat

