from Moyenne import Mean
def CenteredMoment(data,r):
    sum=0
    r=int(r)
    for i in data:
     sum=sum+(pow(i-Mean(data),r))
    cm=sum/len(data)
    return cm