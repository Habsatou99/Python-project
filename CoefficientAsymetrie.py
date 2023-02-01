from EcartType import StD
from Mode import CalculMode
from Moyenne import Mean
def Skewness(data):
 b=(Mean(data)-CalculMode(data))/StD(data)
 return b