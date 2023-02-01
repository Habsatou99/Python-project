from FrequencyByModality import FrequencyByModality

def  CumulativeFrequencyByModality(data,m):
   sum=0
   for i in data:
     if(i<m):
         sum=sum+FrequencyByModality(data,len(data),i)
   sum=sum+FrequencyByModality(data,len(data),m)      
   return sum