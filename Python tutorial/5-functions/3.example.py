## Example

#1- Gönderilen bir klimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız.
"""
def printOnScreen():
    x = input("Kelimeyi giriniz: ")
    count = int(input("Kelimeyi kaç kere girmek istersiniz: "))
    while count>0:
        print(x)
        count-=1
printOnScreen()
"""
##2.yol
"""
def printOnScreen2(kelime,adet):
    kelime = input("Kelimeyi giriniz: ")
    adet = int(int(input("Kaç kere tekrarlanacağını giriniz: ")))
    print(kelime*adet)
"""

# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız.
"""
def convertList(*args):
    liste = []
    for arg in args:
        liste.append(arg)
    return liste
myList = convertList("123",456,"Ömer",789)
print(type(myList))
print(myList)
"""



# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.
# def findPrimeNumber(floorNumber,ceilingNumber):
#     primeNumberList = []
#     while ceilingNumber>=floorNumber:
#         if(ceilingNumber)
# Hatırlatma: remove içine verdiğin parametre değere göre siliyor.
def findPrimeNumber(floor,ceiling):
    floor = int(input("Taban değeri giriniz"))
    ceiling = int(input("Tavan değeri giriniz"))
    myPrimeNumberList = list(range(floor,ceiling+1))
    for x in range(floor,ceiling+1):
        if(x == 1): #1 ise zaten kıyaslama geç
            myPrimeNumberList.remove(1)
            continue
        for y in range(2,x):
            if x%y ==0:
                print(f"Asal değil {x}")
                myPrimeNumberList.remove(x)
                break
    return myPrimeNumberList

print(findPrimeNumber(0,20))

# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürünüz.

def findDivisors(number):
    number = int(input("Bölenlerini bulmak istediğiniz bir sayıyı giriniz: "))
    divisorsOfNumber = []
    for i in range(1,number+1):
        if(number%i == 0):
            divisorsOfNumber.append(i)
    return divisorsOfNumber
print(findDivisors(10))