
"""from array import array
from pickletools import int4
from CoefficientAsymetrie import Skewness
from Covariance import Covariance
from CumulativeFrequencyByModality import CumulativeFrequencyByModality
from EcartType import StD
from FrequencyByModality import FrequencyByModality
#from Gaussienne import Gaussienne

from GenerationVal import GenerationData
from Affichage_Serie import ShowData
from Ecriture import*
from Ecriture1 import writeDataToCsvFile
from Lecture import*
from Lecture1 import readDataFromCsvFile
from Mediane import Median
from Mode import CalculMode
from MomentCentré import CenteredMoment
from Moyenne import Mean
from ObservationsByModality import ObservationsByModality
from Pearson import Correlation
from Variance import Variance
from coefficientApplatissement import Kurtosis
 #Ecriture dans un fichier texte
writeDataToTxtFile("Hello word","Doc2.txt")
#lecture d'un fichier texte
cont=readDataFromTxtFile("Doc1.txt")
print(cont)
#lecture d'un fichier csv
array1=readDataFromCsvFile("Doc3.csv")
print(array1)
array2=[["Nom","Prenom","Ville"]]
#ecriture dans un fichier csv
writeDataToCsvFile(array2,"Doc4.csv")
data1=[10,2,4,6,8,1]
data2=[10,2,4,6,6,1]
data1.sort()
data2.sort()
#affichage d'une serie
ShowData(data1)
min1=int(input("donnez le minimum: "))
max1=int(input("donnez le maximum: "))
N1=int(input("donnez N: "))
#generation de nombres aleatoires
GenerationData(min1,max1,N1)


#effectif d'une modalité
i1=ObservationsByModality(data1,3)
print("le nombre apparait: "+str(i1))
#frequence d'une modalité
i2=FrequencyByModality(data1,len(data1),2)
print("la frequence du nombre est: "+str(i2))
#frequence cumulée d'une modalité
i3=CumulativeFrequencyByModality(data1,2)
print("la frequence cumulée du nombre est: "+str(i3))
#mediane
i11=Median(data1)
print("la mediane du nombre est: "+str(i11))
#moyenne
i4=Mean(data1)
print("la moyenne est: "+str(i4))
#variance
i5=Variance(data1)
print("la variance est: "+str(i5))
#ecart type
i6=StD(data1)
print("l'ecart_type est: "+str(i6))
r=input("donner l'ordre ")
r=int(r)
#moment centré
i7=CenteredMoment(data1,r)
print("le moment centré est: "+str(i7))
#data2=[]

i8=CalculMode(data1)
print("le mode est : "+str(i8))
#Skewness
i9=Skewness(data1)
print("le coefficient d'asymetrie de Pearson est : "+str(i9))
#Kurkosis
i10=Kurtosis(data1)
print("le coefficient d'aplatissement de Pearson est : "+str(i10))
#Covariance
i12=Covariance(data1,data2,len(data1))
print("la covariance est : "+str(i12))
#Correlation
i13=Correlation(data1,data2,len(data1))
print("le Coeficient de Pearson est : "+str(i13))"""




import pandas as pd

from MarginalX import Marginalx
from Marginaley import Marginaly

#create contingence table
df = pd.DataFrame({'X\Y': ['X1', 'X2', 'X3'],

                   'Y1': [100, 0, 0],
                   'Y2': [10, 40, 0],
                   'Y3': [10, 0, 40],
                   })

df0=Marginalx(df)
df2=Marginaly(df)
print(df0)
print(df2)
#IndependanceTheorique
#df3=IndependanceTheorique(df)