class SuperHero():
    def __init__(self,isimInput,yasInput,meslekInput):
        print("Constructer methotu çağrıldı.")
        self.isim=isimInput
        self.yas=yasInput
        self.meslek=meslekInput
superman= SuperHero("Superman",30,"Journalist")
print(superman.isim)
print(superman.meslek)
print(superman.yas)


"""
Yukarıda biz isimInput olarak değer verdik ama normalde verilmez.
Doğrudan değişkenin adı yazılır. İlk dersden kafa karışıklığı 
olmaması için bu seferlik böyle yazdım.
"""