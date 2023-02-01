from Moyenne import Mean
def Variance(data):
    sum=0
    for i in data:
        sum=sum+((i-Mean(data))**2)
    var=sum/len(data)
    return var    