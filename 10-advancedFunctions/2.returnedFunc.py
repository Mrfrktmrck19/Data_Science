### Returned Functions - Fonksiyondan Fonksiyon Döndürme

def takeExponentofNumber(floor):
    def inner(power):
        return floor**power
    return inner

three = takeExponentofNumber(3) #3'ü dış fonksiyona,
print(three(2)) #2'yi iç fonksiyona gönderdik. 




def yetki_sorgula(page):
    def inner(role):
        if role == "Admin":
            return "{0} rolünün {1} sayfasına ulaşabilir.".format(role,page)
        else:
            return "{0} rolün {1} sayfasına ulaşamaz.".format(role,page)
    return inner

user1 = yetki_sorgula("Product Edit")   #dış fonksiyona Product Edit parametresi gönderildi
print(user1("Admin"))   #iç fonksiyona Admin parametresi gönderildi.
print(user1("User"))





def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam+=i
        return toplam

    def carpma(*args):
        toplam = 1
        for i in args:
            toplam*=i
        return toplam
    if islem_adi == "toplama":
        return toplam
    else:
        return carpma



toplama = islem("toplama")

print(toplama(10,20,30,40,50,60,50,45))