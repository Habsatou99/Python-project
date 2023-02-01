from Moyenne import Mean


def Covariance(data,data1,N):
    sum=0
    for i in data1:
     for i in data:
         sum=sum+((i-Mean(data)*i-Mean(data1)))
    k=sum/N
    return k
