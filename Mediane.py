from CumulativeFrequencyByModality import CumulativeFrequencyByModality
def Median(data):
 m=((len(data)/2)+1)
 n=m/len(data)
 for i in data:
  if( CumulativeFrequencyByModality(data,i)>= n):
   j=i
   break
 return j