




class SuperHero():
    def __init__(self,isim,yas,meslek):
        print("Constructer methotu çağrıldı.")
        self.isim=isim
        self.yas=yas
        self.meslek=meslek
    def ornekMethot(self):
        print(f"Ben Süperkahramanım. Adım: {self.isim}")





superman= SuperHero("Superman",30,"Journalist")
print(superman.isim)
print(superman.meslek)
print(superman.yas)
superman.ornekMethot()
