import random
def GenerationData(min,max,N):
  min=int(min)
  max=int(max)
  N=int(N)
  for i in range(N):
   print(random.randint(min,max))