### Decorator Functions
import os
os.system("cls")
"""
Bir fonksiyona özellik eklemek istediğimizde decorator fonksiyonları kullanıyoruz. Peki bu bize ne fayda sağlıyor?
Bir özelliği bir kaç yerde kullanmak istiyorsak bunun için bir decorator fonksiyonu oluşturup bu fonksiyonu bir çok fonksiyon
ile ilişkilendirebiliyoruz. Burada her yazılımcı gibi amacımız daha az kod yazma ve daha özenli yazma.
"""


def my_decorator(func):
    def wrapper(name):  #say hellonun parametresi için.
        print("Fonksiyondan önce olan işlemler")        ## işlemler = özellikler
        func(name)
        print("Fonksiyondan sonraki işlemler")
    return wrapper


#özelik eklemek istediğimiz fonksiyonlar
# @my_decorator, Web Programlama da kullanılabilir.
def sayHello(name):
    print("hello",name)


sayHello = my_decorator(sayHello)
sayHello("ali")

"""
Biz yukarıdaki iki fonksiyona decoratordeki özellikleri ilişkilendirmek istiyoruz.
Yani sayHello fonksiyonunu çağırdığımda dolaylı olarak my_decorator fonksiyonundaki 
özelliklerde tetikleyip çalıştırmak istiyoruz.
Decorator fonksiyonlarının tamamen çalışma mantığı budur.
"""





import math
import time


def my_decorate_zamanHesapla(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish = time.time()
        print("Fonksiyon "+func.__name__+" "+ str(finish-start)+" Saniye sürdü")
    return wrapper

def usalma(a,b):
    print(math.pow(a,b))
    
@my_decorate_zamanHesapla
def faktoriyel(num):
    print(math.factorial(num))

usalma = my_decorate_zamanHesapla(usalma)

usalma(2,3)
faktoriyel(5,5)