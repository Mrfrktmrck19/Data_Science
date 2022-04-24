    ##Fonksiyonlar
def merhabaYaz():
    print("Merhaba")

merhabaYaz()
    ##Fonskiyonlarda Girdi-Çıktı/Input-Return
def merhabaYaz2(isim):
    print(isim)

merhabaYaz2("asdasd")

def merhabaYaz3(isim="Ömer"): ##default değer gelmeli
    print(isim)
merhabaYaz3()
merhabaYaz3("Faruk")


def topla(num1,num2):
    return num1+num2
print(topla(1,2))

    ##Sayısız değişken/parametre alma
##args-kwargs/arguments-key word arguments
def yeniToplama(*args):
    return sum(args)

print(yeniToplama(10,20,30,40))

def bas(*args):
    return args

print(bas(10,20,30,40))##tuple döndürür

def ornekFonksiyon(**kwargs):
    print(kwargs)
ornekFonksiyon(muz=100,elma=200,armut=300) ##sözlükler için kullanılır


def control(**kwargs):
    if "elma" in kwargs:
        print("elma varmış")
    if 100 in kwargs:   ##keywordleri kontrol ediyor
        print("100 varmış")
control(muz=100,elma=200,armut=300)

##başta kaç input alacağımız belli değilse args kwargs kullanmak baya işini kolaylaştırır.