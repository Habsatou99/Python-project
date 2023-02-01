#print('halll')
 
class Personne():
  def __init__(self,nom,age):
    self.nom=nom
    self.age=age
    print("constructeur "+nom)
  def sePresenter(self):
    print("se presenter:")
  def EstMajeur(self):
    if(self.age>=18):
        return True
    else:
        return False

personne1=Personne("jkjk",32)
personne1=Personne("err",36)

personne1.sePresenter()  
#age1=input("donner un age")
x=personne1.EstMajeur()
print(x)
