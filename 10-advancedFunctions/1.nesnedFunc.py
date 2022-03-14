### Nesned Functions - İç İçe Fonksiyonlar
import os
def sayHi(name):
    print("Hi"+name)

asdasd = sayHi

#İki adres bilgiside aynı olacaktır
print(asdasd)
print(sayHi)
#Pythonda objeleri atama yaptığında adreslerin atandığını unutma
sayHi("Ömer")
asdasd("Ömer")

"""
#Çalışır
del asdasd
sayHi("Asdasd sizlere ömür")

#Çalışmaz, asdasd silindi
del asdasd
asdasd("Asdasd sizlere ömür")

#Çalışır, burada sayHi değişkeni silindi yani belleğe ulaşan değişkenlerden biri silindi
#fakat belleğe ulaşan diğer bir değer duruyor. İlgili adresteki veriyi silmiyoruz yani
del sayHi
asdasd("Asdasd sizlere ömür")

"""

#encapsulation
def outer(num1):
    print("outer")
    def inner_increment(num1):
        print("outer")
        return num1+1
    num2= inner_increment(num1) # inner_increment'ı sadece tanımladık, fakat çalıştırmadık bu yüzden bu satırda çalıştırıyoruz
    print(num2)
outer(10)   

#inner_increment fonksiyonunu dış scopta çağırırsan çalışmaz çünkü iç scopte oluşturulup yokediliyor.


os.system("cls")


def factoriel(number):
    if not isinstance(number,int):
        raise TypeError("number parametresi bir sayı olmalıdır.")
    if not number>=0:
        raise ValueError("number parametresi 0 ve ya 0 dan büyük olmalı")

    def inner_factoriel(number):
        if number <=1:
            return 1
        return number * inner_factoriel(number-1)
    result = inner_factoriel(number)
    return result


try:
    print(factoriel(-5))
except Exception as ex:
    print(ex)