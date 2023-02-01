from Covariance import Covariance
from EcartType import StD


def Correlation(data1,data2,N):
    r=Covariance(data1,data2,N)/(StD(data1)*StD(data2))
    return r