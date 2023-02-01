from MomentCentré import CenteredMoment
def Kurtosis(data):
    b2=CenteredMoment(data,4)/(CenteredMoment(data,2)**2)
    return b2