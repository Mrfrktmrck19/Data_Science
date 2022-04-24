##Hem __str__ hem de polyorphism'e iyi bir örnek
class Meyve():
    def __init__(self,isim,kalori):
        self.isim=isim
        self.kalori=kalori
    def __str__(self): ##toString fonksiyonunun aynısı
        return f"İsim: {self.isim}, kalori: {self.kalori}"
    def __len__(self):##bildiğimiz len methotunu değiştirdik
        return self.kalori
    def ekranaBas(self):
        print(self.kalori)

class Elma(Meyve):
    def __init__(self, isim, kalori):
        super().__init__(isim, kalori)


class Muz(Meyve):
    def __init__(self, isim, kalori):
        super().__init__(isim, kalori)

elma= Elma("Elma",150)
muz= Muz("Muz",200)

print(elma)
print(muz)

print(len(muz))
"""
len methotu, toString gibi bözel bir methot olduğu için
objesiz kullanabildik. Mesela şu fonksiyonu objesiz kullanamayız:
ekranaBas()
Çünkü önceden belirlenmiş özel bir fonksiyon değil, biz burada
belirledik.
C++'taki static fonksiyonları hatırlarsın


Bu methotlar magic methots veya special methots
diye internette aratabilirsin.
"""

