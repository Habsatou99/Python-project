from FrequencyByModality import FrequencyByModality
def CalculMode(data):
    max=None
    for i in data:
     if(max is None or FrequencyByModality(data,len(data),i)>max):     
         max=FrequencyByModality(data,len(data),i)
         n=i
    return n
    
    
    