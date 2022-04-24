class Elma():
    def __init__(self,isim):
        self.isim=isim
    def bilgiVer(self):
        return self.isim + "100 kaloridir."

class Muz():
    def __init__(self,isim):
        self.isim=isim
    def bilgiVer(self):
        return self.isim + "150 kaloridir."


elma= Elma("elma")
print(elma.bilgiVer())
muz=Muz("muz")
print(muz.bilgiVer())

meyveListesi = [elma,muz]

for meyve in meyveListesi:
    print(meyve.bilgiVer())

def bilgiAl(meyve):
    print(meyve.bilgiVer())
print("================")
bilgiAl(elma)