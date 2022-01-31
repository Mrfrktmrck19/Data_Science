def changeName(n):
    n = "Ada"       

name = "yiğit"
changeName(name)

print(name)
"""
Terminale baktığında değişken atandığı halde hala değişmediğini göreceksin. Çünkü burada değişkeni döndürmemiz gerekiyor. Bunun yanı sıra, burada referans ile atama konusu var, fonksiyon içerisinde değişken değeri atanıyor ama bir referansla değil.

"""

def change(n):
    n[0] ="istanbul"
cities = ["Ankara","izmir"]
change(cities)
print(cities)
"""
Burada da istanbul larak değiştiğini göreceksin, bunun sebebi daha önce de dediğimiz gibi liste atamaları referans ile gerçekleştiği için yukarda ki fonkisyon ile atama yapabiliyoruz. Hatırlarsan 2 listeden birini diğerine atadığımızda sonra birini değiştirdiğimizde diğerinin de değiştiğini görmüştük. 
"""
print("***********************************************")
sehirler = ["Ankara","İzmir"]
n = sehirler    #liste olduğu için adres kopyalanması oluyor

n[0] = "İstanbul"
print(sehirler)

# adresin kopyalanması değilde içerisindeki verilerin kopyalamasını istersen slicing ile atama yapabilirsin.
print("***********************************************")
sehirler = ["Ankara","İzmir"]
n = sehirler[:]   #içerisindeki değerler kopyalanacak. Adres değil! Bu yüzden artık ikisi ramde farklı yerleri gösterecek.
                # n = sehirler[0:2] ' ilk 2 indextekileri kopyalıyor 
n[0] = "İstanbul"
print(sehirler)


#sınırsız parameter:
def add(*params):
    return sum(params)
print(add(10,20,30,4,0,5,0,60))

def add(*params):
    sum = 0
    for i in params:
        sum+=i
    return sum
print(add(10,20,30,4,0,5,0,60))


##bir dictionary almak istediğimizde:
def displayUser(**args):
    print(type(args))
    for key,val in args.items():
        print(f"{key} is {val}")

displayUser(name= 'Çınar', age = 2, city = 'istanbul')
displayUser(name= 'Ada', age = 12, city = 'kocaeli', phone = '123132')
displayUser(name= 'Yiğit', age = 14, city = 'ankara', phone = '123132', email= 'yigit@gmail.com')


print("**************************************")

def myFunc(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10, 20, 30, 40, 50, 60, 70, key1 = 'value 1', key2 = 'value 2')