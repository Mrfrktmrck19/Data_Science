#method
"""
Bir sınıf altındaki fonksiyonlara method diyoruz
"""
myList = [1,2,3,4,5,6,7,8,9,10]
myList.append(11) #burada append myList değişkeninin kalıtım aldığı "List" sınıfının bir fonksiyonudur. Yani bir methottur.
print(type(myList))



myStr = "Asdasd"
myStr.capitalize() #method
print(myStr)

#! Python method/fonksiyonlarını https://www.python.org/doc/ adresinden bulabilirsin.


#function
"""
Fonksiyonlar zaten bildiğin üzere belirli bir amaca hizmet eden kod topluluğu/blokları. Başka yerlerde subroutine (alt programlama) diye de duyabilirsin. Fonksiyonları yazarken tek bir işlev vermeye çalışırız. Çünkü SOLID ilkelerinden de hatırlayacağın üzere ileri bir tarihte kodu güncelleyeceğin zaman sorun çıkartabilir.
"""

#function tanımlanması
def sayHello():
    print("Hello There")
sayHello()

def sayHello(name):
    print(f"Hello There {name}")
sayHello("Ömer")

def sayHello(name = "Ömer"):    #default değer tanımlanmış hali
    print(f"Hello There {name}")
sayHello()

def sayHello(name = "Ömer"):    #default değer tanımlanmış hali
    print(f"Hello There {name}")
sayHello("Ahmet")

def sayHello(name):
    return "Hello"+name
msg = sayHello("Ömer") # yada değişkene atamadan direk print içerisinde de yazdırabilirsin
print(msg)

def sum (num1,num2):
    return num1+num2
print(sum(5,6))