"""print("je m'appelle toto  ")
nom=input("quel est ton nom? ")
print(nom)

print("donnez la valeur de n ")
ageprochain=0

while ageprochain==0:
    age=input("quel est votre age ")
    try:
        ageprochain=int(age)+1
    except:
        print('erreur, entrez un age normal')

    else:      
         print("votre age prochain est et votre actuel est"+str(age))"""
def demander_nom():
 reponse_nom=""

 while reponse_nom == "":
    reponse_nom=input("donnez le nom")
     
 return reponse_nom
  


nom=demander_nom()
print(nom) 
