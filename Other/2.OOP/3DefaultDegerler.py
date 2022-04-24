class Kopek():
    yilCarpani=7
    def __init__(self,yas=5): ##default değer atadık
        self.yas=yas
    def kopekYasHesapla(self):
        return self.yas*self.yilCarpani##Kopek.yiCarpani'da yapabilirdik.

myDog= Kopek()
print(myDog.kopekYasHesapla())
