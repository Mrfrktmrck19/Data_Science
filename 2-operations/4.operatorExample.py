# 1- Girilen 2 sayıdan hangisi büyüktür ?
import email
from unittest import result


# a = int(input("İlk sayıyı giriniz: "))
# b = int(input("İkinci sayıyı giriniz: "))

# if a>b:
#     print(f"a (yani{a} b'den (yani{b}) büyüktür")
# elif a<b:
#     print(f"b (yani{b}) a'den (yani{a}) büyüktür")
# else:
#     print(f"a ile be birbirine eşittir (yani {a} == {b})")


# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
# vize1 = int(input("İlk vize notu: "))
# vize2 = int(input("İkinci vize notu: "))
# final = int(input("Final notu: "))
# total =((vize1+vize2)*3/10 + final*2/5)
# result = ((vize1+vize2)*3/10 + final*2/5) >50

# if result:
#     print(f"Dersi geçti, ortalaması: {total}")
# else:
#     print(f"Dersten kaldı, ortalaması: {total}")


# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.
# a = int(input("Sayı giriniz: "))
# result = a%2 ==0
# if result:
#     print(f"{a} çift")
# else:
#     print(f"{a} tek")

# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.
a = int(input("Sayı giriniz: "))
result = a>=0
if result:
    print(f"{a} pozitif")
else:
    print(f"{a} negatif")



# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.

email = "mrfrktmrck@gmail.com"
password = "123"

girilenEmail = input('email: ')
girilenPassword = input('parola: ')

isEmail = (email == girilenEmail.lower().strip())
isPassword = (password == girilenPassword.lower())

print(f'Email bilgisi doğrumu: {isEmail} ve Parola doğru mu: {isPassword}')