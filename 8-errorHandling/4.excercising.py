### Uygulama
import re
from unittest import result
myList = ["1","2","5a","10b","abc","10","20"]

# 1 -> Find numeric chars in list

# for item in myList:
#     if re.search("[1-9]",item): #unutma, değişşken tipine değil texteki metine bakıyoruz
#         print(item)

# for x in myList:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue



# 2 -> Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı 
# olduğundan emin olunuz aksi halde hata mesajı yazın.


while True:
    num = input("sayı: ")
    if num == "q":
        break
    
    try:
        result = float(num)
        print("Girdiğiniz sayı: ",num)
        break
    except Exception as ex:
        print("Geçersiz sayı. Hata: ",ex)
        continue    #zaten devam edecekte anlam açısından koymak iyi


# 3 -> Girilen parola içinde türkçe karakter hatası veriniz.

turkishChar = "ığüşİçö"
psw = input("parola: ")
for i in psw:
    if i in psw:
        raise TypeError("PArola Türkçe karakter içeremez")
    else:
        pass
print("Geçerli parola")

# 4 -> Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için
# hata mesajları verin.


def faktoriyel(x):
    x = int(x)

    if x < 0:
        raise ValueError('Negatif değer')

    result = 1

    for i in range(1, x+1):
        result *= i

    return result

for x in [5, 10, 20, -3, '10a']:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)
        continue 
    print(y)